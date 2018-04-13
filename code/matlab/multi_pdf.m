clear;clc;
x = load('cyf_phone.txt');
% x2 = load('jzp_phone_tcp_transRate.txt');
% x3 = load('wz_phone_tcp_transRate.txt');

% x1 = x(:,3); %IAT
% x1_indices = find(x1>1.2*10^6);
% x1(x1_indices) = [];
% x2_indices = find(x2>1.2*10^6);
% x2(x2_indices) = [];
% x3_indices = find(x3>1.2*10^6);
% x3(x3_indices) = [];
%     


[f1, x1i] = ksdensity(x1);
% [f2, x2i] = ksdensity(x2);
% [f3, x3i] = ksdensity(x3);
% plot(x1i, f1,'r-*', x2i, f2, 'b-o', x3i,f3, 'g-v')
plot(x1i, f1,'b-*')
xlabel('IAT','FontSize',18);
ylabel('probability density function','FontSize',18);
% hleg = legend('cyf','jzp','wz');
% set(hleg,'FontSize',18);

