clear;clc;
x1 = load('cyf_phone_tcp_transRate.txt');
x2 = load('jzp_phone_tcp_transRate.txt');
x3 = load('wz_phone_tcp_transRate.txt');

% x1 = x1(:,3); %IAT
x1_indices = find(x1>1.2*10^6);
x1(x1_indices) = [];


x2_indices = find(x2>1.2*10^6);
x2(x2_indices) = [];

x3_indices = find(x3>1.2*10^6);
x3(x3_indices) = [];
    


[f1, x1i] = ksdensity(x1);
% x1i = 0:1000:1.2*10^6;
% x2i = 0:1000:1.2*10^6;
% x3i = 0:1000:1.2*10^6;
% f1 = ksdensity(x1, x1i);
% f2 = ksdensity(x2, x1i);
% f3 = ksdensity(x2, x1i);
[f2, x2i] = ksdensity(x2);
[f3, x3i] = ksdensity(x3);
plot(x1i, f1,'r-*', x2i, f2, 'b-o', x3i,f3, 'g-v')
% axis([0 inf 0 inf]);
xlabel('传输速率','FontSize',18);
ylabel('概率密度','FontSize',18);
hleg = legend('Device-1','Device-2','Device-3');
set(hleg,'FontSize',18);

