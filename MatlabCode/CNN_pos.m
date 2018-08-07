% CNN POS test
clc
% clear all

% YTrain=csvread('2018-03-30 17:21:10.725046.csv');
% X=imageDatastore('~/CNN/Position');
% YTrain=csvread('C:\Users\EazyE\Desktop\drimages_pos\Position\2018-03-30 17_21_10.725046.csv');
% X=imageDatastore('C:\Users\EazyE\Desktop\drimages_pos\pos\2018-03-30 17_21_10.725046');
% YTrain = csvread('C:\Users\EzraLaptop\Desktop\drimages_pos\Position\2018-03-30 17_21_10.725046.csv');
% X=imageDatastore('C:\Users\EzraLaptop\Desktop\drimages_pos\pos\2018-03-30 17_21_10.725046');

addpath('~/Dropbox/ML/SemesterProject/CNN_POS/Functions')
% YTrain = csvread('~/DR2/drimages/Position/2018-03-30 17:21:10.725046.csv');
% X=imageDatastore('~/DR2/drimages/pos/2018-03-30 17:21:10.725046');

YTrain = csvread('/home/ez/DR2/drimages/Position/2018-06-01 17:47:25.838371.csv',0,0,[0,0,9999,1]);
% YTrain2=csvread('/home/ez/DR2/drimages/Position/2018-06-01 16:28:39.727672.csv',0,0,[0,0,4999,3]);
YTrain = cat(1,YTrain,csvread('/home/ez/DR2/drimages/Position/2018-06-13 12:23:15.006233.csv',0,0,[0,0,9999,1]));
% YTrain2=cat(1,YTrain2,csvread('/home/ez/DR2/drimages/Position/2018-06-12 21:01:06.889173.csv',0,0,[0,0,4999,3]));
YTrain = cat(1,YTrain,csvread('/home/ez/DR2/drimages/Position/2018-06-15 17:22:13.481537.csv',0,0,[0,0,9999,1]));
% YTrain2=cat(1,YTrain2,csvread('/home/ez/DR2/drimages/Position/2018-06-18 12:19:33.755903.csv',0,0,[0,0,4999,3]));
YTrain = cat(1,YTrain,csvread('/home/ez/DR2/drimages/Position/2018-07-03 15:43:49.129033.csv',0,0,[0,0,9999,1]));
YTrain = cat(1,YTrain,csvread('/home/ez/DR2/drimages/Position/2018-07-03 20:33:03.537759.csv',0,0,[0,0,9999,1]));


X=imageDatastore({'/home/ez/DR2/drimages/pos/2018-06-01 17:47:25.838371',...
    '/home/ez/DR2/drimages/pos/2018-06-13 12:23:15.006233',...
    '/home/ez/DR2/drimages/pos/2018-06-15 17:22:13.481537',...
    '/home/ez/DR2/drimages/pos/2018-07-03 15:43:49.129033',...
    '/home/ez/DR2/drimages/pos/2018-07-03 20:33:03.537759'});
% X2=imageDatastore({'/home/ez/DR2/drimages/pos/2018-06-01 16:28:39.727672','/home/ez/DR2/drimages/pos/2018-06-12 21:01:06.889173','/home/ez/DR2/drimages/pos/2018-06-18 12:19:33.755903'});

X.Files=natsortfiles(X.Files);
% X2.Files=natsortfiles(X2.Files);
% X.ReadFcn = @(loc)imresize(imread(loc),[224,224]);
XTrain = [X.Files];% X2.Files];
% YTrain = num2cell(YTrain);
% YTrain = mat2cell(YTrain,ones(length(YTrain),1),2);
% YTrain2=reshape(YTrain2',2,[])';
% YTrain2=mat2cell(YTrain2,2*ones(length(YTrain2)/2,1));
% YTrain=[YTrain];% YTrain2];

% XTrain2=imread(X,:);

%%
idx = randperm(length(YTrain),1000);
XValidation = XTrain(idx);
XTrain(idx) = [];
YValidation = YTrain(idx,:);
YTrain(idx,:) = [];
XTrain=table(XTrain,YTrain(:,1),YTrain(:,2),'VariableNames',{'Files','X','Y'});
XValidation=table(XValidation,YValidation(:,1),YValidation(:,2),'VariableNames',{'Files','X','Y'});
% clear YTrain YValidation ;
% XT=zeros(224,224,3,9000);
% XV=zeros(224,224,3,1000);
% for i = 1:length(XTrain)
%    XTrain2(:,:,:,i) = readimage(char(XTrain),i);
%      XT(:,:,:,i) = imresize(imread(char(XTrain(i))),[224,224]);
% end
% for i =1:length(XValidation)
%     XV(:,:,:,i) = imresize(imread(char(XValidation(i))),[224,224]);
% end   
% XT=double(XT);
%%

layersT =d1.detector.Network.Layers(1:end-3);
layers= [
        layersT
        fullyConnectedLayer(2)
        regressionLayer];
layers(37) = maxPooling2dLayer(2,'Stride',2,'Padding',0);
% layers(38) = fullyConnectedLayer(256);
% layers(41) = fullyConnectedLayer(64);

% net = googlenet; 
% lgraph=layerGraph(net);
% lgraph = removeLayers(lgraph, {'loss3-classifier','prob','output'});
% 
% newLayers = [
%     fullyConnectedLayer(2,'Name','fc','WeightLearnRateFactor',10,'BiasLearnRateFactor',10)
%     regressionLayer('Name','RegressionOUT')];
% lgraph = addLayers(lgraph,newLayers);
% lgraph = connectLayers(lgraph,'pool5-drop_7x7_s1','fc');
%{
net = vgg16;
layersT = net.Layers(1:end-3);
layers= [
        layersT
        fullyConnectedLayer(1)
        regressionLayer];
%}
delete d1;
clear d1;
%%

% numTrainImages = numel(YTrain(:,1));
% figure
% idx = randperm(numTrainImages,20);
% for i = 1:numel(idx)
%     subplot(4,5,i)    
%     imshow(XTrain(:,:,:,idx(i)))
%     drawnow
% end
%%

miniBatchSize  = 32;
validationFrequency = floor(numel(YTrain(:,1))/miniBatchSize);
options = trainingOptions('adam',...
    'MiniBatchSize',miniBatchSize,...
    'MaxEpochs',9,...
    'InitialLearnRate',1e-4,...
    'LearnRateSchedule','piecewise',...
    'LearnRateDropFactor',0.1,...
    'LearnRateDropPeriod',4,...
    'Shuffle','every-epoch',...
    'ValidationData',XValidation,...
    'ValidationFrequency',validationFrequency,...
    'ValidationPatience',3,...
    'ExecutionEnvironment','gpu',...
    'Verbose',1,...
    'VerboseFrequency',128,...
    'L2Regularization',0.005,...
    'CheckpointPath','/home/ez/Dropbox/ML/SemesterProject/CNN_POS/Functions/NNCheckpoint');
net = trainNetwork(XTrain,{'X','Y'},layers,options);
%%

pred = predict(net,XValidation,'MiniBatchSize',32,'ExecutionEnvironment','gpu');
predError= XValidation{:,2:3}-pred;
numCorrect = sum(abs(predError)<1.5);
numValidationImages = height(XValidation);
accuracy = numCorrect/numValidationImages
% for i = 1:10
%     img=imread(XTrain.Files{i});
%     pred = predict(net,img);
%     figure
%     imshow(img);
%     title(pred);
% end

