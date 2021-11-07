clear
clc
close all

GP_num=[2*pi];
GP_den=[1 2*pi];
GP=tf(GP_num,GP_den);

figure
bode(GP)
figure
hold on
rlocus(sys)


%settling time


plot([-0.2 -0.2],[-1.5 1.5],'r-','LineWidth',1)
plot([-1 0],[tan(53.14*pi/180) 0],'b-', 'LineWidth',1)
plot([-1 0],[-tan(53.14*pi/180) 0],'b-', 'LineWidth',1)