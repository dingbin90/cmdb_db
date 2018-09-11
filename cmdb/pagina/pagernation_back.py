class Pagina(object):
    def __init__(self,totalCount,currentPage,perPageNum=3,maxPagenum=5):
        self.total_count = totalCount  #数据总个数
        try:
            self.current_page = currentPage  #当前页
        except Exception as e:
            self.current_page = 1
        self.per_pagenum = perPageNum  #每页显示行数
        self.max_pagenum = maxPagenum  #最多显示页面
    @property
    def start(self):
        return (self.current_page-1)*self.per_pagenum
    @property
    def end(self):
        return self.current_page*self.per_pagenum
    @property
    def num_page(self):
        '''总页数'''
        a,b = divmod(self.total_count,self.per_pagenum)#divmod方法回显示2个值比如divmode(66,10),显示（6，6）
        if b == 0:  #拿第二个值比较，如果是0，则总页数等于a，否则等于a+1
            return a
        return a+1

    def page_range(self):   #获取分页的信息
        if self.num_page < self.max_pagenum:
            return range(1,self.num_page+1)

        one_of_part = int(self.max_pagenum/2)

        if self.current_page < one_of_part:
            return range(1,self.max_pagenum+1)

        if self.current_page+one_of_part > self.num_page:
            return range(self.num_page-self.max_pagenum,self.num_page+1)
        return range(self.current_page-one_of_part,self.current_page+one_of_part+1)

    def page_str(self):
        page_list = []
        if self.current_page == 1:
           page_pre = "<a href='#'>上一页</a>"
        else:
            page_pre = "<a href='/cmdb/asset?p=%s>上一页</a>"%(self.current_page-1)
        page_list.append(page_pre)
        for i in self.page_range():
            a = "<a href='/cmdb/asset?p=%s>%s</a>"%(i,i)
            page_list.append(a)
        if self.current_page == self.num_page:
            page_next = "<a href='#'>上一页</a>"
        else:
            page_next = "<a href='/cmdb/asset?p=%s>上一页</a>"%(self.current_page+1)
        page_list.append(page_next)
        return ''.join(page_list)

