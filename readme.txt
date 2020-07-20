实现功能：获取目标网站linked包含的公司员工信息。
实施步骤：  1、通过百度搜索获取员工信息Url。
            2、利用浏览器自动化打开保存网页信息。后缀格式为.htm(网站源元素信息)
            3、解析所以保存的.htm页面。
            4、使用搜索脚本从解析到的数据中进行匹配。

python脚本文件说明；
getUrl.py                   通过百度获取目标员工Url。         input:company.txt(目标公司名称)    output:allurl.txt(所有Url Link)
save_html.py                操作浏览器保存打开的Url信息.      input:allurl.txt                   output:xxxxx.htm
analyze_html.py             解析xxxxx.htm                     input:xxxxx.htm                    output:result.txt
search_QT(Python3.7.x).py   有GUI搜索脚本。                   input:result.txt                   output:SearchResult.txt(单次搜索结果)
search.py                   无GUI搜索脚本                     默认input:company.txt              output:SearchResult.txt(company.txt包含公司所有结果)

版本说明：以上脚本除search_QT(Python3.7.x).py 使用Pyhton3.7.x 其它脚本均为2.7.x版本
