re = load('bayes_result.txt');
p = re(:,1);
r = re(:,2);
f = re(:,3);


f_indices = find(f<0.8)
p(f_indices) = [];
r(f_indices) = [];
f(f_indices) = [];
p_mean = mean(p(1:50));
r_mean = mean(r(1:50));
f_mean = mean(f(1:50));
s = [num2str(p_mean),',  ',num2str(r_mean),',  ',num2str(f_mean)]
