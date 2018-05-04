clear;clc;
device_FS = load('feature\wz_iphone5_2_frameSize.txt');
device_IAT = load('feature\wz_iphone5_2_IAT.txt');
device_TR = load('feature\wz_iphone5_2_transRate.txt');
data = [device_FS device_IAT device_TR];

fid = fopen('mix_feature\wz_iphone5_2.txt', 'w');
[col, row] = size(data);
for i=1:col
    for j = 1:row-1
        fprintf(fid,'%f,', data(i,j));
    end
    fprintf(fid, '%f', data(i,j));
    fprintf(fid, '\n');
end
fclose(fid);