library("rvest")
library(stringr)
library(magrittr)
url <- "http://www.cheyun.com/" #车云
web <- read_html(url)

#提取htmLnodes
news <- web%>%html_nodes("div.m-infos-news.m-infos-news1.fn-right")%>%html_nodes("h3")%>%html_nodes("a") #注意这里有两级类名的，可以直接用第一类的 
#提取新闻标题存入title
title<- news%>%html_text()
#提取网页的url存入link
link <- news%>%html_attr("href")

for (i in 1:length(link)){
  link[i] <- str_c("http://www.cheyun.com",link[i])
}

article <- c(1:length(link))

for(i in 1:length(link)) #抓取所有提取的新闻的内容
{
  web<-read_html(link[i]) #注意这里可能需要根据不同网站的encoding来指定编码方式  read_hmtl(url,encoding=)
  article_nodes<-web%>%html_nodes("div.m-con-article.m-con-special p") #注意这里有很多P，如何把所有P的内容都拼接在一起
  paras<-article_nodes%>%html_text()
  article[i]<-paste(paras[1:length(paras)],collapse = "")
}

newsdata<-data.frame(link=link,title=title,article=article)
write.csv(newsdata,file = "newscheyun.csv",fileEncoding = "UTF-8",row.names = FALSE)