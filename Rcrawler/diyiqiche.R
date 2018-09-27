library("rvest")
library(stringr)
library(magrittr)
url <- "https://www.d1ev.com/" #第一电动
web <- read_html(url)

#提取htmLnodes
news1 <- web%>%html_nodes("a.ws-newsflash-cont")
#提取新闻标题存入title
title1<- news1%>%html_text()
#提取网页的url存入Link1
link1 <- news1%>%html_attr("href")

nodes_two<-"div.article--content.am-fl"
news2<- web%>%html_nodes(nodes_two)%>%html_node("a") #可以提取所有nodes_two中的第一个a
title2<- news2%>%html_text()
link2 <- news2%>%html_attr("href")


#组合所有的title 以及link

title<-title1%>%append(title2) #管道操作,连接所有的title以及link
link<-link1%>%append(link2)

for(i in 1:length(link)){
  if( str_detect(link[i],"https")==FALSE)
  link[i]<-str_c("https://www.d1ev.com",link[i])
}


article <- c(1:length(link))

for(i in 1:length(link)) #抓取所有提取的新闻的内容
{
  web<-read_html(link[i]) #注意这里可能需要根据不同网站的encoding来指定编码方式  read_hmtl(url,encoding=)
  article_nodes<-web%>%html_nodes("div#showall233 p") #注意这里有很多P，如何把所有P的内容都拼接在一起
  paras<-article_nodes%>%html_text()
  article[i]<-paste(paras[1:length(paras)-1],collapse = "")
}


newsdata<-data.frame(link=link,title=title,article=article)
write.csv(newsdata,file = "newsdiyidiandong.csv",fileEncoding = "UTF-8",row.names = FALSE) #这里写入的编码一定要是UTF-8,否则在使用PYTHON分词处理时会出现乱码
