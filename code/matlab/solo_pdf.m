clear;clc;
data = load('jzp_phone.txt');
x = data(:,3); %IAT

%%
%����ɢ��ͼ
% plot(1:size(x,1),x,'*m')

%%
% ����transRate�Ĺ���Ч��ͼ
% x1_indices = find(x>1400);
% x(x1_indices) = [];
subplot(1,2,1)
plot(1:size(x,1),x,'*')
axis([0 inf 0 inf])
title('����ǰ','FontSize',10)
ylabel('TransRate','FontSize',10);

x1_indices = find(x>1.2*10^6);
x(x1_indices) = [];
subplot(1,2,2)
plot(1:size(x,1),x,'*')
axis([0 inf 0 15*10^8])
title('�����','FontSize',10)
ylabel('TransRate','FontSize',10);

%%
% %����frameSize�Ĺ���Ч��ͼ
% x1_indices = find(x>1400);
% x(x1_indices) = [];
% subplot(1,2,1)
% plot(1:size(x,1),x,'*')
% axis([0 inf 0 1500])
% title('����ǰ','FontSize',10)
% ylabel('FrameSize','FontSize',10);
% 
% x1_indices = find(x>100);
% x(x1_indices) = [];
% subplot(1,2,2)
% plot(1:size(x,1),x,'*')
% axis([0 inf 0 1500])
% title('�����','FontSize',10)
% ylabel('FrameSize','FontSize',10);
%%
%���Ʋ�ͬ��ֵ�Ĺ���Ч��ͼ��IAT��
% subplot(2,2,1)
% plot(1:size(x,1),x,'*')
% axis([0 inf 0 1.6])
% title('δ����','FontSize',18)
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
%%-----��������x��pdf����
% [f, xi] = ksdensity(x);
% plot(xi, f,'b-*')
% title('threshold = 0.6','FontSize',18)
% xlabel('IAT','FontSize',18);
% ylabel('probability density function','FontSize',18);
%%


