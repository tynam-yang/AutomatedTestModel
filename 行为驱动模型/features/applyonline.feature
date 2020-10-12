Feature: 技术顾问预约测试

    Scenario: 打开技术顾问预约网站
        When 打开访问的网页 "https://www.grapecity.com.cn/applyonline"
        Then 进入了技术顾问预约网站成功

    Scenario: 技术顾问预约测试
        When 输入姓名 "test"、电话 "13666666666"、邮箱 "test@grapecity.com"、公司全称 "西安XXXX有限公司"、职务 "技术爱好者"、感兴趣产品 "SpreadJS 纯前端表格控件"、
        内容描述 "学习使用" 然后进行预约
        Then 技术顾问预约成功