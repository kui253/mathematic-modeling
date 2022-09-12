Data=xlsread('C.xlsx')%%作为原始数据
data=Data(:,1)
closed=Data(:,2)

%%如果有缺失值，插值法（线性插值）
yuan=[closed(1,1):closed(end,1)]'
meiyong=zeros(length(yuan),1)
yuan=[yuan meiyong]
queshi=zeros((length(yuan)-length(data)),1)
i=1,j=1,k=1;
while i<=closed(end,1)
if yuan(i,1)==Data(j,1)
      yuan(i,2)=Data(j,2)
j=j+1;
else
    queshi(k,1)=yuan(i,1)
    k=k+1;
end
i=i+1;
end

yi＝interpl (Data(:,1),Data(:,2),queshi, 'linear')%%线性插值
i=1,j=1;
while i<=length(yuan(:,1))
    if yuan(i,2)==0
        yuan(i,2)=yi(j,1)
        j=j+1;
    end
    i=i+1;
end
%%至此，插值结束，yuan就是插值后的数据

biaozhuncha=std(yuan(:,2));%%标准差
guiyihua=(yuan(:,2)-sum(yuan(:,2))./length(yuan(:,2)))./biaozhuncha%%归一化

out=adftest(数据);%%结果是0则不平稳，是1则平稳
d数据=diff(数据);%%如果不平稳，则差分，再检验

Mdl = arima(p, d, q);  %第二个变量值为d阶差分(平稳)
EstMdl = estimate(Mdl,data);
[forData,YMSE] = forecast(EstMdl,step,'Y0',data);  %%step指预测的步数 fordata是预测值，YMSE是预测值的方差

[P Q]=findPQ(dClosed,7,7)%%qq图


figure(1), autocorr(x);%%自相关
figure(2), parcorr(x);%%偏相关


xlswrite('文件名',数据)