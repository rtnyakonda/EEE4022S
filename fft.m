[data, fs] = audioread("C:\Users\Reginald Nyakonda\Desktop\Recording.m4a");
N = length(data);
data_fft =fft(data,N);
F = ((0:1/N:1-1/N)*fs);
data_shift = fftshift(data_fft);
fshift = (-N/2:N/2-1)*(fs/N);

plot(fshift, abs(data_fft));
title('Frequency plot');
ylabel("Magnitude");
xlabel("Freq (Hz)");