clear;clc;
x = load('G:\graduate_git\code\Classifier\combine\frameSize.txt');

% x1 = x(:,1); %IAT
% x1_indices = find(x1>0.05);
% x1(x1_indices) = [];

% x1 = x(:,2); %IAT
% x1_indices = find(x1>200);
% x1(x1_indices) = [];

% x1 = x(:,3); %transrite
% x1_indices = find(x1>1.2*10^6);
% x1(x1_indices) = [];


[f1, x1i] = ksdensity(x1);
% [f2, x2i] = ksdensity(x2);
% [f3, x3i] = ksdensity(x3);
% plot(x1i, f1,'r-*', x2i, f2, 'b-o', x3i,f3, 'g-v')
plot(x1i, f1,'b-*')
xlabel('IAT','FontSize',18);
ylabel('probability density function','FontSize',18);
% hleg = legend('cyf','jzp','wz');
% set(hleg,'FontSize',18);

