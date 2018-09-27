library("rvest")
library(stringr)
url <- "http://www.indunet.net.cn/" #中国工业网
web <- read_html(url)
News <- web%>%html_nodes("li.list-group-item a") #这个地方不需要划分特别细致

#提取新闻标题
title<- News%>%html_text()


#提取网页的url
link <- News%>%html_attr("href")


for(i in 1:length(link)){
 
   link[i]<-str_c("http://www.indunet.net.cn",link[i])
}

article <- c(1:length(link))

for(i in 1:length(link)) #抓取所有提取的新闻的内容
{
  web<-read_html(link[i])
  article_nodes<-web%>%html_nodes("div#content-text p") #注意这里有很多P，如何把所有P的内容都拼接在一起
  paras<-article_nodes%>%html_text()
  article[i]<-paste(paras[1:length(paras)-1],collapse = "")
}


newsdata<-data.frame(link=link,title=title,article=article)
write.csv(newsdata,file = "newsgongye.csv",fileEncoding = "UTF-8",row.names = FALSE) #这里写入的编码一定要是UTF-8,否则在使用PYTHON分词处理时会出现乱码
