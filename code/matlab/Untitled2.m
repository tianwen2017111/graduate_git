clear;clc;
s = 'wz_iphone5_2';
x = load('G:\graduate_git\code\Classifier\combine\frameSize.txt');
d_x = load('G:\graduate_git\code\Classifier\Data\wz_iphone5_2.txt');

% IAT = x(:,1);
% FS = x(:,2);
% TR = x(:,3);
n = size(x,1);

d_IAT = d_x(:,1);
d_FS = d_x(:,2);
d_TR = d_x(:,3);
d_n = size(d_x,1);
% 
x1_indices = find(d_FS>100);
d_FS(x1_indices) = [];
% y = d_IAT(1:500);
% y = IAT;

plot(1:200,d_FS(1:200),'b*')