% CNN POS test
clc
% clear all

% YTrain=csvread('2018-03-30 17:21:10.725046.csv');
% X=imageDatastore('~/CNN/Position');
% YTrain=csvread('C:\Users\EazyE\Desktop\drimages_pos\Position\2018-03-30 17_21_10.725046.csv');
% X=imageDatastore('C:\Users\EazyE\Desktop\drimages_pos\pos\2018-03-30 17_21_10.725046');
% YTrain = csvread('C:\Users\EzraLaptop\Desktop\drimages_pos\Position\2018-03-30 17_21_10.725046.csv');
% X=imageDatastore('C:\Users\EzraLaptop\Desktop\drimages_pos\pos\2018-03-30 17_21_10.725046');

addpath('~/Dropbox/ML/SemesterProject/CNN_POS/Functions');
% YTrain = csvread('~/DR2/drimages/Position/2018-05-18 20:30:23.116154.csv',0,2);
% YTrain2= csvread('/home/ez/DR2/drimages/Position/2018-05-23 17:21:11.005688.csv');
YTrain = csvread('/home/ez/DR2/drimages/Position/2018-06-01 17:47:25.838371.csv',0,2);
YTrain = cat(1,YTrain,csvread('/home/ez/DR2/drimages/Position/2018-06-13 12:23:15.006233.csv',0,2));
YTrain = cat(1,YTrain,csvread('/home/ez/DR2/drimages/Position/2018-06-15 17:22:13.481537.csv',0,2));
YTrain = cat(1,YTrain,csvread('/home/ez/DR2/drimages/Position/2018-07-03 15:43:49.129033.csv',0,2));
YTrain = cat(1,YTrain,csvread('/home/ez/DR2/drimages/Position/2018-07-03 20:33:03.537759.csv',0,2));

YTrain2=csvread('/home/ez/DR2/drimages/Position/2018-06-01 16:28:39.727672.csv');
YTrain2=cat(1,YTrain2,csvread('/home/ez/DR2/drimages/Position/2018-06-12 21:01:06.889173.csv'));
YTrain2=cat(1,YTrain2,csvread('/home/ez/DR2/drimages/Position/2018-06-18 12:19:33.755903.csv'));
YTrain2 = cat(1,YTrain2,csvread('/home/ez/DR2/drimages/Position/2018-07-02 17:46:51.089760.csv'));
YTrain2 = cat(1,YTrain2,csvread('/home/ez/DR2/drimages/Position/2018-07-03 19:39:18.921559.csv'));

% X=imageDatastore('~/DR2/drimages/pos/2018-05-18 20:30:23.116154');
% X2=imageDatastore('/home/ez/DR2/drimages/pos/2018-05-23 17:21:11.005688');
X=imageDatastore({'/home/ez/DR2/drimages/pos/2018-06-01 17:47:25.838371',...
    '/home/ez/DR2/drimages/pos/2018-06-13 12:23:15.006233',...
    '/home/ez/DR2/drimages/pos/2018-06-15 17:22:13.481537',...
    '/home/ez/DR2/drimages/pos/2018-07-03 15:43:49.129033',...
    '/home/ez/DR2/drimages/pos/2018-07-03 20:33:03.537759'});
X2=imageDatastore({'/home/ez/DR2/drimages/pos/2018-06-01 16:28:39.727672',...
    '/home/ez/DR2/drimages/pos/2018-06-12 21:01:06.889173',...
    '/home/ez/DR2/drimages/pos/2018-06-18 12:19:33.755903',...
    '/home/ez/DR2/drimages/pos/2018-07-02 17:46:51.089760',...
    '/home/ez/DR2/drimages/pos/2018-07-03 19:39:18.921559'});

X.Files=natsortfiles(X.Files);

X2.Files=natsortfiles(X2.Files);
% X.ReadFcn = @(loc)imresize(imread(loc),[224,224]);

Bolt1Pos = YTrain2(:,1:2);
Bolt2Pos = YTrain2(:,3:4);
BoltPixPos = YTrain2(:,5:end)';
BoltPixPos = reshape(BoltPixPos,4,[])';

%%%%% Expand Bounding boxes to fit minimum
for i=1:length(YTrain)
   YTrain(i,3) = YTrain(i,3)*3.2;
   YTrain(i,4) = YTrain(i,4)*2.5;
   YTrain(i,1) = YTrain(i,1)-(YTrain(i,3)/3);
   YTrain(i,2) = YTrain(i,2)-(YTrain(i,4)/3);
end

for i=1:length(BoltPixPos)
   BoltPixPos(i,3) =BoltPixPos(i,3)*3.2;
   BoltPixPos(i,4) = BoltPixPos(i,4)*2.5;
   BoltPixPos(i,1) = BoltPixPos(i,1)-(BoltPixPos(i,3)/3);
   BoltPixPos(i,2) = BoltPixPos(i,2)-(BoltPixPos(i,4)/3);
end
YTrain=round(YTrain);
idx = YTrain(:,1) < 0;

i= 1;

%%%%% Take out data with bounding boxes outside image
while sum(idx) > 0
    if idx(i) == 1
        YTrain(i,:) = [];
        X.Files(i,:)=[];
        idx(i) = [];
        continue
    end
    i=i+1;
end

idx = YTrain(:,2) < 0;

i= 1;
while sum(idx) > 0
    if idx(i) == 1
        YTrain(i,:) = [];
        X.Files(i,:)=[];
        idx(i) = [];
        continue
    end
    i=i+1;
end        

%%%%% Search for 
idx2 = size(YTrain);
idx3 = length(BoltPixPos);
idx4 = zeros(sum(BoltPixPos(:,1)<0)+sum(BoltPixPos(:,2)<0),1);
k=1;
YTrainCon=mat2cell(YTrain,ones(idx2(1),1),4);
YTrainCon2= mat2cell(BoltPixPos,2*ones(idx3/2,1));
for i = 1:length(YTrainCon2)
%     disp(YTrainCon2{i});
%     disp(i);
        if YTrainCon2{i}(1,1) < 0 || YTrainCon2{i}(2,1)< 0 || YTrainCon2{i}(1,2)< 0 || YTrainCon2{i}(2,2) <0
           idx4(k)=i;
           k=k+1;
        end
end
idx4= idx4(find(idx4~=0));
YTrainCon2(idx4)=[];
X2.Files(idx4)=[];
XTrain = [X.Files; X2.Files];
YTrainCon=[YTrainCon;YTrainCon2];


x=table(XTrain,YTrainCon,'VariableNames',{'Filenames','Bolt'});
% % XTrain2=imread(X,:);
%%
% for k = 10000:10050
% I = imread((x.Filenames{k}));
% 
% % Insert the ROI labels.
% I = insertShape(I, 'Rectangle', x.Bolt{k});
% 
% % Resize and display image.
% % I = imresize(I, 3);
% figure
% imshow(I)
% % end
%%

idx = floor(0.9 * height(x));
trainingData = x(1:idx,:);
testData = x(idx:end,:);
%%
 % % For continuing Layers
% d2=load('Test2_448_20_Jun_18.mat');
layers=d2.detector.Network.Layers;
clear Bolt1Pos Bolt2Pos PoltPixPos i idx idx2 idx3 idx4 k YTrain YTrain2 YTrainCon2
%%
 % % For New layers
% net=vgg16;
% conv1Weight=single(randn([3,3,3,32])*0.01);
% conv2Weight=single(randn([3,3,32,32])*0.01);
% conv3Weight=single(randn([3,3,32,64])*0.01);
% 
% conv1Bias=single(randn([1,1,32])*0.01);
% conv2Bias=single(randn([1,1,32])*0.01);
% conv3Bias=single(randn([1,1,64])*0.01);
% 
% layersT = net.Layers(1:end-3); layersT= layersT(3:end);
% layersU =[    
%     imageInputLayer([448 448 3],'Name','Input Size of 448x448,3')
%     convolution2dLayer(3,32,'Stride',1,'Padding',1,'WeightLearnRateFactor',20,'BiasLearnRateFactor',20,'WeightL2Factor',1)
%     reluLayer('Name','ReLU_1')
%     convolution2dLayer(3,32,'Stride',1,'Padding',1,'WeightLearnRateFactor',20,'BiasLearnRateFactor',20,'WeightL2Factor',1)
%     reluLayer('Name','ReLU_2')
%     maxPooling2dLayer(2,'Stride',2,'Padding',0)
%     convolution2dLayer(3,64,'Stride',1,'Padding',1,'NumChannels',32,'WeightLearnRateFactor',20,'BiasLearnRateFactor',20,'WeightL2Factor',0)];
% layersU(2).Weights=conv1Weight;
% layersU(2).Bias=conv1Bias;
% layersU(4).Weights=conv2Weight;
% layersU(4).Bias=conv2Bias;
% layersU(7).Weights=conv3Weight;
% layersU(7).Bias=conv3Bias;
% layers = [
%     layersU
%     layersT
%     fullyConnectedLayer(2,'WeightLearnRateFactor',20,'BiasLearnRateFactor',20)
%     softmaxLayer
%     classificationLayer];

% layers([40, 43])=[];


%%
% data =
% load('/tmp/faster_rcnn_stage_1_checkpoint__4500__2018_05_11__16_31_26.mat')
miniBatchSize  = 256;
% validationFrequency = floor(numel(YTrain(:,1))/miniBatchSize);
% max epochs 2,6,4,4
options1 = trainingOptions('sgdm',...
    'MiniBatchSize',miniBatchSize,...
    'MaxEpochs',1,...
    'InitialLearnRate',1e-4,...
    'LearnRateSchedule','piecewise',...
    'LearnRateDropFactor',0.1,...
    'LearnRateDropPeriod',2,...
    'ExecutionEnvironment','gpu',...
    'Verbose',1,...
    'VerboseFrequency',256,...
    'CheckpointPath','/home/ez/Dropbox/ML/SemesterProject/TestRCNN/NNCheckpoint');
options2 = trainingOptions('sgdm',...
    'MiniBatchSize',miniBatchSize,...
    'MaxEpochs',1,...
    'InitialLearnRate',1e-4,...
    'LearnRateSchedule','piecewise',...
    'LearnRateDropFactor',0.1,...
    'LearnRateDropPeriod',3,...
    'ExecutionEnvironment','gpu',...
    'Verbose',1,...
    'VerboseFrequency',256,...
    'CheckpointPath','/home/ez/Dropbox/ML/SemesterProject/TestRCNN/NNCheckpoint');
options3 = trainingOptions('sgdm',...
    'MiniBatchSize',miniBatchSize,...
    'MaxEpochs',1,...
    'InitialLearnRate',1e-4,...
    'LearnRateSchedule','piecewise',...
    'LearnRateDropFactor',0.1,...
    'LearnRateDropPeriod',2,...
    'ExecutionEnvironment','gpu',...
    'Verbose',1,...
    'VerboseFrequency',256,...
    'CheckpointPath','/home/ez/Dropbox/ML/SemesterProject/TestRCNN/NNCheckpoint');
options4 = trainingOptions('sgdm',...
    'MiniBatchSize',miniBatchSize,...
    'MaxEpochs',1,...
    'InitialLearnRate',1e-4,...
    'LearnRateSchedule','piecewise',...
    'LearnRateDropFactor',0.1,...
    'LearnRateDropPeriod',2,...
    'ExecutionEnvironment','gpu',...
    'Verbose',1,...
    'VerboseFrequency',256,...
    'CheckpointPath','/home/ez/Dropbox/ML/SemesterProject/TestRCNN/NNCheckpoint');
options = [
    options1
    options2
    options3
    options4];
    detector = trainFasterRCNNObjectDetector(trainingData, layers, options, ...
        'NegativeOverlapRange', [.1 0.5], ...
        'PositiveOverlapRange', [0.6 1]);
    
    
 %%
% Run detector.
close all
% k=144;
ll = randperm(26802,50);
for ii=1:20
k=ll(ii);

% j= k+26801;
j=k;
% Resize and display image.
l = imread(x.Filenames{j});
I = insertShape(l,'Rectangle',x.Bolt{j});
figure
subplot(1,2,2);
imshow(I)

 img = imread(trainingData.Filenames{k});
[bbox, score, label] = detect(d1.detector, img);
% [bbox3, score3, label3] = detect(detector3, img);
idx2= score>=0.65;
% idx3 = score3>=0.65;
if length(idx2)<= 1 && idx2 == 0
% bbox
% % Display detection results.
else
detectedImg = insertObjectAnnotation(img, 'Rectangle', bbox,score);
subplot(1,2,1);
imshow(detectedImg);
end

% if length(idx3) <= 1 && idx3 == 0
% else
% detectedImg3 = insertObjectAnnotation(img, 'Rectangle', bbox3(idx3,:),score3(idx3));
% subplot(1,3,2);
% imshow(detectedImg3);
% end
end
%%
%{
doTrainingAndEval = true;
if doTrainingAndEval
    % Run detector on each image in the test set and collect results.
    resultsStruct = struct([]);
    for i = 1:height(testData)
        
        % Read the image.
        I = imread(testData.Filenames{i});
        
        % Run the detector.
        [bboxes, scores, labels] = detect(d1.detector, I);
        
        % Collect the results.
        resultsStruct(i).Boxes = bboxes;
        resultsStruct(i).Scores = scores;
        resultsStruct(i).Labels = labels;
    end
    
    % Convert the results into a table.
    results = struct2table(resultsStruct);

end

% Extract expected bounding box locations from test data.
expectedResults = testData(:, 2:end);

% Evaluate the object detector using Average Precision metric.
[ap, recall, precision] = evaluateDetectionPrecision(results, expectedResults);


hold on
plot(recall,precision)
xlabel('Recall')
ylabel('Precision')
grid on
title(sprintf('Average Precision = %.2f', ap))
%}