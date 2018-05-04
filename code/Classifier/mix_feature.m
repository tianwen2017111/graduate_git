clear;clc;
device_FS = load('feature\ytw_ipad_frameSize.txt');
device_IAT = load('feature\ytw_ipad_IAT.txt');
device_TR = load('feature\ytw_ipad_transRate.txt');
data = [device_FS device_IAT device_TR];

fid = fopen('mix_feature\ytw_ipad.txt', 'w');
[col, row] = size(data);
for i=1:col
    for j = 1:row-1
        fprintf(fid,'%f,', data(i,j));
    end
    fprintf(fid, '%f', data(i,j));
    fprintf(fid, '\n');
end
fclose(fid);