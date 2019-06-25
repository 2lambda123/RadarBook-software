%% Gaussian noise pd example
% Created by: Lee A. Harrison
% On: 10/11/2018

clear, clc

% Set the parameters
snr_db = linspace(3.0, 18.0);
snr = 10.^(snr_db/10);
pfa = 1.0e-6;

% Calculate the probability of detection
pd = pd_gaussian(snr, pfa);

% Plot the results
figure;
plot(snr_db, pd);
title('Pd - Gaussian Noise');
xlabel('Signal to Noise (dB)');
ylabel('Probability of Detection');
grid on;
plot_settings;