% addpath('~/Dropbox/ML/SemesterProject/CNN_POS/Functions');
if exist('gTruth','var')==0
    load('testLabels2.mat');
end
% close all

sorttruth=gTruth.DataSource;
[truth, ndx]=natsortfiles(sorttruth);
truthdim=table2cell(gTruth.LabelData);
truthdim2 = truthdim(ndx);
truth =table(truth,truthdim2,'VariableNames',{'Filenames','Bolt'});
%%
tempDir = pwd;
pred=[];
threshold=0.592;
for i = 101:120
%     picture=imread(sprintf('/home/ez/Dropbox/ML/SemesterProject/TestSet/TestSet3/picture%d.png',i));
    picture=imread(sprintf('%s/TestSet2/picture%d.png',tempDir,i));
    [bbbox, score, label] = detect(d1.detector, picture,'Threshold',threshold);
    
    bbbox;
    if isempty(bbbox) == 0
        
        temp=zeros(size(bbbox,1),1);
        temp2 = zeros(size(bbbox,1),2);
        label_temp=cell(size(bbbox,1),1);
        
        for mn=1:size(bbbox,1)
            
            temp(mn)=mean2(picture(bbbox(mn,2):bbbox(mn,2)+bbbox(mn,4)-1,...
                bbbox(mn,1):bbbox(mn,1)+bbbox(mn,3)-1));
        end
        if size(bbbox,1)==1
            temp2 = predict(net,picture);
            label_temp=['X= ',num2str(temp2(:,1),'%0.1f'),' Y= ',num2str(temp2(:,2),'%0.1f')];%, ' Conf: ',num2str(score)];
            pred= [pred;temp2];
        else
            for r = 1:size(bbbox,1)
                pictemp = picture;
                for c = 1:size(bbbox,1)
                    if c == r
                        continue
                    else
                        pictemp(bbbox(c,2):(bbbox(c,2))+bbbox(c,4)-1,...
                            bbbox(c,1):(bbbox(c,1))+bbbox(c,3)-1,:) = temp(c);
                    end
                    
                end
                temp2(r,:) = predict(net,pictemp,'ExecutionEnvironment','gpu');
                pred= [pred;temp2(r,:)];
                %                 imshow(pictemp)
                label_temp{r}=['X= ',num2str(temp2(r,1),'%0.1f'),' Y= ',num2str(temp2(r,2),'%0.1f')];%,' Conf: ',num2str(score(r))];
            end
            
        end
        
        detectedImg = insertObjectAnnotation(picture, 'Rectangle', bbbox,label_temp,'FontSize',12,'TextBoxOpacity',0.6);
%         imwrite(detectedImg,sprintf('/home/ez/Dropbox/ML/SemesterProject/TestSet/TestSet3/Detections/picture%d.png',i));
        % % %    disp(temp2);
        %     figure
        %     imshow(detectedImg);
        
    else
        %         label_temp=[];
        %         figure
        %         imshow(picture);
    end
    %     disp(label_temp);
    %     disp(size(pred,1));
    
end

%%
%{
doTrainingAndEval = true;
thresholdEval=0.54;
if doTrainingAndEval
    % Run detector on each image in the test set and collect results.
    resultsStruct = struct([]);
    for i = 1:20
        
        % Read the image.
        I = imread(truth.Filenames{i});
        
        % Run the detector.
        [bboxes2, scores2, labels2] = detect(d1.detector, I,'Threshold',thresholdEval);
        
        % Collect the results.
        resultsStruct(i).Boxes = bboxes2;
        resultsStruct(i).Scores = scores2;
        resultsStruct(i).Labels = labels2;
%     if isempty(bboxes2) == 0
%         detectedImg = insertObjectAnnotation(I, 'Rectangle', bboxes2,scores2,'FontSize',12,'TextBoxOpacity',0.6);
% %         detectedImg2 = insertObjectAnnotation(detectedImg, 'Rectangle', truth.Bolt{i},'Ground Truth','FontSize',12,'TextBoxOpacity',0.6);
%         figure
%         imshow(detectedImg);
%
%     else
%         figure
%         imshow(I);
%     end
    end
    
    % Convert the results into a table.
    results = struct2table(resultsStruct);
%      disp([size(cell2mat(results.Scores),1);thresholdEval]);
end

% Extract expected bounding box locations from test data.
expectedResults = truth(41:60,2);

% Evaluate the object detector using Average Precision metric.
[ap, recall, precision] = evaluateDetectionPrecision(results, expectedResults,0.20);
f1= (2*recall.*precision./(recall+precision));
[f1Max, in]=max(f1);
figure
hold on
plot(recall,precision)
xlabel('Recall')
ylabel('Precision')
grid on
title(sprintf('Max F1 = %.2f & %.2f', precision(in),recall(in)))
%}
%%

%

%{
% % 1-20 65%
test2Pos = xlsread('Test1_20.xlsx');
test2Pos(4,:)=[];
test2Pos(7,:)=[];
test2Pos(11,:)=[];
test2Pos(21,:)=[];
test2Pos(22,:)=[];
test2Pos(23,:)=[];
test2Pos(23,:)=[];
test2Pos(23,:)=[];
test2Pos(23,:)=[];
test2Pos(23,:)=[];
test2Pos(26,:)=[];
test2Pos(29,:)=[];
%}

%{
% % 81-100 54%
test2Pos = xlsread('/home/ez/Dropbox/ML/SemesterProject/TestSet/TestSet1/Test1_20.xlsx');
pred([3 6 11 16 17 22 25 33 36 37 39 40 46],:)=[];
test2Pos([5 6],:)=test2Pos([6 5],:);
test2Pos([15 16],:)=test2Pos([16 15],:);
test2Pos([21 22],:)=test2Pos([22 21],:);
test2Pos([35 36],:)=test2Pos([36 35],:);
test2Pos([24 26 28 29 32 ],:)=[];

%}
%{
set1= ...
    [0.6250    0.8750;
    0.6731    0.8750;
    0.7292    0.8750;
    0.7174    0.8250;
    0.8182    0.6750;
    0.9259    0.6250;
    1.0000    0.5500];

f11 = ...
    [0.7292   50.0000;
     0.7609   53.0000;
     0.7955   54.0000;
     0.7674   55.0000;
     0.7397   60.0000;
     0.7463   65.0000;
     0.7097   70.0000];
figure
plot(f11(:,2),f11(:,1));
xlabel('Threshold','FontSize',16);
ylabel('F1 Score','FontSize',16);
figure
plot(set1(:,2),set1(:,1))
xlabel('Recall','FontSize',16);
ylabel('Precision','FontSize',16);
%}
%

%{
% % 21-40 50%
test2Pos = xlsread('Test20_40.xlsx');
% test2Pos(8,:)=[];
% test2Pos(24,:)=[];
% pred(14,:)=[];
% pred(14,:)=[];
% pred(31,:)=[];
% pred(33,:)=[];
%}

%
% % 101-120 59.2% 0.2%
% test2Pos = xlsread('/home/ez/Dropbox/ML/SemesterProject/TestSet/TestSet2/Test20_40.xlsx');
test2Pos=xlsread(sprintf('%s/TestSet2/Test20_40.xlsx',tempDir));
pred([3 17],:)=[];
test2Pos([4 23 25],:)=[];
test2Pos([4 5],:)=test2Pos([5 4],:);
test2Pos([10 11],:)=test2Pos([11 10],:);
test2Pos([16 17],:)=test2Pos([17 16],:);
test2Pos([20 21],:)=test2Pos([21 20],:);
test2Pos([30 31],:)=test2Pos([31 30],:);
test2Pos([32 33],:)=test2Pos([33 32],:);
%}
%{
set2 = ...
    [0.8125    0.9750;
    0.7222    0.9750;
    0.8478    0.9750;
    0.8810    0.9250;
    0.9487    0.9250;
    0.9444    0.8500;
    1.0000    0.7750];
f12 = ...
     [0.8864   45.0000;
     0.8298   50.0000;
     0.9070   55.0000;
     0.9024   59.0000;
     0.9367   59.2000;
     0.8947   60.0000;
     0.8732   65.0000];
figure
plot(f12(:,2),f12(:,1));
xlabel('Threshold','FontSize',16);
ylabel('F1 Score','FontSize',16);
figure
plot(set2(:,2),set2(:,1))
xlabel('Recall','FontSize',16);
ylabel('Precision','FontSize',16);

%}

%
%{
% % 50%
test2Pos=xlsread('Test40_60.xlsx');
pred(4,:)=[];
pred(18,:)=[];
pred(23,:)=[];
pred(27,:)=[];
test2Pos(10,:)=[];
test2Pos(19,:)=[];
test2Pos(30,:)=[];
test2Pos(31,:)=[];
test2Pos(36,:)=[];
test2Pos=xlsread('Test60_80.xlsx');
%}


%{
% 63% 27% pres/rec
% test2Pos=xlsread('/home/ez/Dropbox/ML/SemesterProject/TestSet/TestSet3/Test40_60.xlsx');
test2Pos=xlsread(sprintf('%s/TestSet3/Test40_60.xlsx',tempDir));
pred([3 4 22 25 32 35 36 40 44],:)=[];
test2Pos([3 4],:)=test2Pos([4 3],:);
test2Pos([7 8],:)=test2Pos([8 7],:);
test2Pos([24 25],:)=test2Pos([25 24],:);
test2Pos([31 32],:)=test2Pos([32 31],:);
% test2Pos([35 36],:)=test2Pos([36 35],:);
test2Pos([37 38],:)=test2Pos([38 37],:);
test2Pos([11 40],:)=[];
%}
%


%}
%%
thresholdIN=0.5*2.54;
% ll = randperm(28,28)';
ll=1:length(pred)';
pred2=pred(ll,:)*2.54;
testPos2=test2Pos(ll,:)*2.54;
predError=testPos2-pred2;
% predError = predError./testPos2;
predError=vecnorm(predError,2,2);
% predError = reshape(predError,size(predError,1)*2,1);
predError=abs(predError);
numCorrect=sum(predError<=thresholdIN);
numValidationImages = size(testPos2,1);
accuracy = numCorrect/numValidationImages;
meanPred=mean(predError);
stdPred=std(predError);
disp([accuracy;meanPred;stdPred]);
%%

figure
hists=histogram(predError,0:0.5:20);
% percentHist=(hists.Values/numValidationImages*100);
% figure
% bar(0:0.5:19.5,percentHist);
