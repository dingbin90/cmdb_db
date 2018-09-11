(function () {
    requestUrl = null;
    function Next_Page() {
            $('#pager li').each(function () {

                if ($(this).hasClass('active')){
                    //console.log($(this).text())
                    var num = $(this).text()
                    var num2 = Number(num) + Number(1)
                    console.log('num2',num2)
                    pageinit(num2)
                }
            })

    }
    function ChangePage() {
            $('#pager li').each(function () {

                if ($(this).hasClass('active')){
                    //console.log($(this).text())
                    var num = $(this).text()
                    pageinit(num-1)
                }
            })

    }
    //给选中的a标签加上class=active的属性
    function initaddclass(num) {
         $('#pager li a ').each(function () {
             var text = $(this).text();
             if (text == num) {
                // console.log('ok',text,num)
                 $(this).parent().addClass('active')
             }else {
                 //console.log('no',text,num)
             }

         })

    }
    //绑定分页事件
    function bindChangpager() {
        $('#pager').on('click','a',function () {
            var num = $(this).text();

            pageinit(num);


        })
    }
     //删除绑定事件
    function binddelete() {
        $('#iddelete').click(function () {
            var del_list = [];//声明要删除的列表
            $('#table_td').find(":checkbox").each(function () {   //找扫所有的checkbox 循环
                if ($(this).prop("checked")){   //若果checkbox是选中的
                    var $curtr = $(this).parent().parent();   //所选中的checkbox的tr标签
                    var id = $($curtr).attr('row-id');   //找到tr row-id的值
                    alert(id);
                    del_list.push(id)   //把id加到列表中
                }

            });
            $.ajax({
                url:requestUrl,  //发送的url
                type:"delete",   //方式的delete
                data:JSON.stringify(del_list),   //序列化数据
                dataType:'json',  //发送的方式是json
                success:function (args) {   //回调函数
                    if (args.status){
                        alert(args.status);
                        init()
                    }else {
                        alert(args.error);
                    }

                }
            })
        })

    }
     //保存绑定事件
    function bindSave() {
        $('#idSave').click(function () {
            var postList = [];//发送后台更新数据得列表
            $('#table_td').find('tr[has-edit="true"]').each(function () {
                //$(this)  >等于tr
                var temp = {};
                var id = $(this).attr('row-id');
                //alert(id);
                temp["id"] = id;
                //alert(temp);
                $(this).children('[edit-enable="true"]').each(function () {
                    //$(this) 等于 td
                    var name = $(this).attr('name');
                    var origin = $(this).attr('origin');
                    var newVal = $(this).attr('new-val');
                    //alert(origin,newVal)
                if (origin != newVal){
                    temp[name] = newVal;
                    //alert(temp)
                };

                });
                    postList.push(temp);

            });
               //console.log(postList);
            //alert(postList)
            $.ajax({
                url:requestUrl,
                //url:'/cmdb/asset-json/',注释：如果写成/cmdb/asset-json会报错500，后面要加斜线
                type:'put',
                contentType: "application/json; charset=utf-8",
                //data:{"post_list":JSON.stringify(po_list)},
                data:JSON.stringify(postList),
                traditional:true,
                dataType:'json',
                success:function (arg) {
                    if(arg.status){
                        alert(arg.status)
                        init(1);

                }else {
                    alert(arg.error);
                    }
                }
            });

        })

    }
    //进入编辑按钮绑定事件
    function bindMenus(){
        $("#idEditMode").click(function () {
            var editng = $(this).hasClass('btn-warning');
            if (editng){
                //推出编辑
                $(this).removeClass('btn-warning');
                $('#table_td').find(':checked').each(function () {
                    var $currentTr = $(this).parent().parent();
                   // $currentTr.removeClass('success');
                    trouteditmode($currentTr);

                })
            }
            else {
                //进入编辑
                $(this).addClass('btn-warning');
                $('#table_td').find(':checked').each(function () {
                    var $currentTr = $(this).parent().parent();
                   // $currentTr.addClass('success');
                    trintoeditmode($currentTr);

                })
            }

        })
    }
    //绑定checkbox事件
    function bindCheckbox(){
        $('#table_td').on('click',':checkbox',function () {
            if ($("#idEditMode").hasClass("btn-warning")){
              var ck = $(this).prop('checked');
              var $currentTr = $(this).parent().parent();
            if (ck){
                //进入编辑模式
               // console.log("进入编辑模式");
               // $currentTr.addClass('success');
                trintoeditmode($currentTr);
            }else {
                //退出编辑模式
                //$currentTr.removeClass('success');
              //  console.log('退出编辑模式');
                trouteditmode($currentTr);
            }
            }


        })
    }
    //进入编辑模式
    function trintoeditmode($tr){
        $tr.addClass('success');
        $tr.attr('has-edit','true');
        $tr.children().each(function () {
            var editEnable = $(this).attr('edit-enable');
            var editType = $(this).attr('edit-type'); //拿到edit-type的属性，
            var origin = $(this).attr('origin');
            if(editEnable){

                if (editType == 'select'){
                    var globalNname = $(this).attr('global-name');//获取全局变量
                    var sel = document.createElement('select');
                    sel.className = 'form-control';




                    $.each(window[globalNname],function (k1,v1) {
                            var op = document.createElement('option')
                            op.setAttribute('value',v1[0]);
                            op.innerHTML = v1[1];
                            $(sel).append(op)

                    });
                    $(sel).val(origin)
                    $(this).html(sel)

                }
                else if (editType == 'input'){
                    var inenerText = $(this).text();
                var tag = document.createElement('input');
                //设置tag就是input的class属性
                tag.className = 'form-control';
                //设置tag就是input的的宽度
                tag.style.width = '%100';
                tag.value = inenerText;
                $(this).html(tag);
                }

            }

        })

    }
    //推出编辑模式
    function trouteditmode($tr){
            //找到tr里面所有的孩子（td），然后循环td
            $tr.removeClass('success');
            $tr.children().each(function () {
                //$(this)=td
                var editEnable = $(this).attr('edit-enable');
                var editTypr = $(this).attr('edit-type');
                if (editEnable){
                    if (editTypr == 'select'){
                        //获取正在编辑得select对象
                        var $select = $(this).children().first();
                        //获取选中得option得id
                        var newId = $select.val();
                        //获取当前选中option得文本
                        var newText = $select[0].selectedOptions[0].innerHTML;
                        $(this).html(newText);
                        var origin = $(this).attr('origin');
                        $(this).attr('new-val',newId);
                    }else if (editTypr == 'input'){
                             //推出编辑模式
                    var $input = $(this).children().first();
                    var inputvalue = $input.val();
                    $(this).html(inputvalue);
                    $(this).attr('new-val',inputvalue)   ;
                    }

                }

            })

    }
    String.prototype.format_s = function (kwargs) {
       var ret = this.replace(/\{(\w+)\}/g,function (km,m) {
            return kwargs[m];

        });
        return ret
    };
    //全选按钮绑定得事件
    function bindcheckall() {
        $('#Checkall').click(function () {
            $('#table_td').find(':checkbox').each(function () {
                if ($('#idEditMode').hasClass('btn-warning')){
                    if ($(this).prop('checked')){
                        //已选中的checkbox
                        }else {
                     $(this).prop('checked',true);
                    $currentTr = $(this).parent().parent();
                    trintoeditmode($currentTr);
                    }

                }else {
                    $(this).prop('checked',true);
                }


            })

        })

    }
    //取消按钮绑定事件
    function bindcancelall() {
        $('#Cancelall').click(function () {
            $('#table_td').find(':checkbox').each(function () {
            if ($('#idEditMode').hasClass('btn-warning')){
              //  var $currentTr = $(this).parent().parent();
                if ($(this).prop('checked')){
                    $(this).prop('checked',false);
                    var $currentTr = $(this).parent().parent();
                    trouteditmode($currentTr)

                }else {
                    //如果在编辑模式下，checkbox没有选中不做操作
                }


            }else {
                $(this).prop('checked',false);
            }

        })
        })


    }
    //反选按钮绑定事件
    function bindFanxuan(){
        $('#Fanxuan').click(function () {
            //找到table下所有的checkbox，然后循环
            $("#table_td").find(':checkbox').each(function () {
                //判断是否在编辑的模式
                if ($("#idEditMode").hasClass('btn-warning')){
                    //判断如果checkbox是选中的
                    if ($(this).prop('checked')){
                        //取消checkbox的选中状态
                        $(this).prop('checked',false);
                        //找到tr的标签，退出编辑模式
                       var $currentTr = $(this).parent().parent();
                       trouteditmode($currentTr);
                    }else {
                        //else判断checkbox不是选中的情况
                        $(this).prop('checked',true);
                        var $currentTr = $(this).parent().parent();
                        trintoeditmode($currentTr)
                    }

                }else {
                    //判断不再编辑模式的情况
                    if ($(this).prop('checked')){
                        $(this).prop('checked',false);
                    }else {
                        $(this).prop('checked',true);
                    }
                }

            })

        })

    }
    //点击页码初始化
    function pageinit(page) {
        //console.log(page)
        $.ajax({
            url: requestUrl,
            type: 'GET',
            data: {'page': page},
            dataType: 'json',
            success: function (result) {
                initGlobalData(result.global_dict);
                initHeader(result.table_config);
                initBody(result.table_config, result.data);
                initPager(result.pager);
                initaddclass(page);
            }
        });
    }
    //初始化table
    function init(page) {

      $.ajax({
          url:requestUrl,
          type:'GET',
          data:{'page':page},
          dataType:'json',
          success:function (result) {
              //console.log(result);
              initGlobalData(result.global_dict);
              initHeader(result.table_config);
              initBody(result.table_config,result.data);
              initPager(result.pager);
             // initaddclass(page);
          }
      });
    }
    //初始化分页的页码
    function initPager(pager) {

        $('#pager').html(pager);


    };
    //生成head
    function initHeader(table_config) {
     var tr = document.createElement('tr');
     $.each(table_config, function (k, item) {
         if (item.display){
             var th = document.createElement('th');
             th.innerHTML = item.title;

             $(tr).append(th);
         }


     });
     $("#table_th").empty();
     $("#table_th").append(tr);

 };
    //生成body
    function initBody(table_config,data) {
        $("#table_td").empty();
        //循环data，生成每一行数据
        $.each(data,function (k,row) {
            var tr = document.createElement('tr');
            tr.setAttribute('row-id',row['id']);
            //循环配置文件，生成没一列数据
            $.each(table_config,function (i,colconfig) {

                if(colconfig.display){

                var td = document.createElement('td');
                var kwargs = {}
                $.each(colconfig.text.kwargs,function (key,value) {
                    if (value.substring(0,2)=="@@"){
                        var globalName = value.substring(2,value.length);
                        var currentID = row[colconfig.q];
                        var t = getTextGlobalById(globalName,currentID);
                        kwargs[key]=t;

                    }
                    else if (value[0]== "@"){
                        kwargs[key] = row[value.substring(1,value.length)]
                    }
                    else {
                        kwargs[key]=value;
                    }


                });
                var temp = colconfig.text.content.format_s(kwargs);

                td.innerHTML = temp;
                $.each(colconfig.attrs,function (kk,vv) {
                    if (vv[0] == '@'){
                        td.setAttribute(kk,row[vv.substring(1,vv.length)]);
                    }else {
                         td.setAttribute(kk,vv);
                    }


                });
                $(tr).append(td)
                }

            });
            $("#table_td").append(tr)
        });

 };
    //生成全局变量
    function initGlobalData(global_dict) {
      $.each(global_dict,function (k,v) {
        //生成全局变量
         window[k]=v

      })

 }
    //生成choice字段的文本
    function getTextGlobalById(globalName,currentID) {
       // console.log(globalName)
    var ret = null;
     $.each(window[globalName],function (k,item) {

        // console.log(item[0],item[1],currentID);
         if (item[0] == currentID){
             ret = item[1];
             return
         }

     });
     return ret;
 }
    //jQuery 扩展方法，触发得接口
    jQuery.extend({
        'DB':function (url) {
            requestUrl = url;
            init(1);
            bindMenus();
            bindCheckbox();
            bindcheckall();
            bindcancelall();
            bindFanxuan();
            bindSave();
            binddelete();
            bindChangpager();


        },

        'change':function (url) {
             ChangePage();

        },
        'next':function (url) {
            Next_Page();
        }
    })

})()