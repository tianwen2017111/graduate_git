clear;clc;
data = load('jzp_phone.txt');
x = data(:,3); %IAT

%%
%绘制散点图
% plot(1:size(x,1),x,'*m')

%%
% 绘制transRate的过滤效果图
% x1_indices = find(x>1400);
% x(x1_indices) = [];
subplot(1,2,1)
plot(1:size(x,1),x,'*')
axis([0 inf 0 inf])
title('降噪前','FontSize',10)
ylabel('TransRate','FontSize',10);

x1_indices = find(x>1.2*10^6);
x(x1_indices) = [];
subplot(1,2,2)
plot(1:size(x,1),x,'*')
axis([0 inf 0 15*10^8])
title('降噪后','FontSize',10)
ylabel('TransRate','FontSize',10);

%%
% %绘制frameSize的过滤效果图
% x1_indices = find(x>1400);
% x(x1_indices) = [];
% subplot(1,2,1)
% plot(1:size(x,1),x,'*')
% axis([0 inf 0 1500])
% title('降噪前','FontSize',10)
% ylabel('FrameSize','FontSize',10);
% 
% x1_indices = find(x>100);
% x(x1_indices) = [];
% subplot(1,2,2)
% plot(1:size(x,1),x,'*')
% axis([0 inf 0 1500])
% title('降噪后','FontSize',10)
% ylabel('FrameSize','FontSize',10);
%%
%绘制不同阈值的过滤效果图（IAT）
% subplot(2,2,1)
% plot(1:size(x,1),x,'*')
% axis([0 inf 0 1.6])
% title('未过滤','FontSize',18)
% ylabel('IAT','FontSize',18);
% 
% x1_indices = find(x>0.6);
% x(x1_indices) = [];
% subplot(2,2,2)
% plot(1:size(x,1),x,'*')
% axis([0 inf 0 1.6])
% title('threshold = 0.6','FontSize',18)
% ylabel('IAT','FontSize',18);

% x1_indices = find(x>0.4);
% x(x1_indices) = [];
% subplot(2,2,3)
% plot(1:size(x,1),x,'*')
% axis([0 inf 0 1.6])
% title('threshold = 0.4','FontSize',18)
% ylabel('IAT','FontSize',18);
% 
% x1_indices = find(x>0.2);
% x(x1_indices) = [];
% subplot(2,2,4)
% plot(1:size(x,1),x,'*')
% axis([0 inf 0 1.6])
% title('threshold = 0.2','FontSize',18)
% ylabel('IAT','FontSize',18);

%%
%%-----绘制向量x的pdf曲线
% [f, xi] = ksdensity(x);
% plot(xi, f,'b-*')
% title('threshold = 0.6','FontSize',18)
% xlabel('IAT','FontSize',18);
% ylabel('probability density function','FontSize',18);
%%


