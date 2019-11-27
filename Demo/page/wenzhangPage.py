from Demo.base.basePage import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class Wenzhangguanli(WebDriver):
    """  新增文章  """

    # 所属栏目
    # channel_loc = (By.XPATH, '//*[@id="CmsInfo_channelId"]/option[3]')
    channel_loc = (By.XPATH, '//*[@id="CmsInfo_channelId"]/option[3]')
    # 标题
    infoTitle_loc = (By.ID, 'CmsInfo_infoTitle')
    # 来源
    comeFrom_loc = (By.ID, 'comeFrom')
    # 文章类型
    articleType_loc = (By.XPATH, '//*[@id="articleType"]/option[1]')
    # 来源地址
    comeFromAddress_loc = (By.ID, 'comeFromAddress')
    # 作者
    CmsInfo_author_loc = (By.ID, 'CmsInfo_author')
    # 作者单位
    authorOrg_loc = (By.NAME, 'authorOrg')
    # 是否置顶
    isTop_loc = (By.ID, 'isTop')
    # 发布时间
    CmsInfo_issueDate_loc = (By.ID, 'CmsInfo_issueDate')
    # 封面图片
    uploadify_loc = (By.ID, 'uploadify')
    # 文章内容
    infoContent_loc = (By.ID, 'ueditor_0')
    # 保存按钮
    chickArticle_loc = (By.XPATH, '//*[@id="saveSubmit1"]')
    # 提交审核按钮
    saveSubmit2_loc = (By.ID, 'saveSubmit2')

    def typeChannel(self):
        # s1 = Select(self.findElement(*self.channel_loc))
        # # for i in s1:
        # #
        # #     print('*'*10, s1.select_by_index(i))
        # s1.select_by_index(3)
        # time.sleep(2)
        self.findElement(*self.channel_loc)

    def typeInfoTitle(self, infoTitle):
        self.findElement(*self.infoTitle_loc).send_keys(infoTitle)

    def typeComeFrom(self, comeFrom):
        self.findElement(*self.comeFrom_loc).send_keys(comeFrom)

    def typeArticleType(self, articleType):
        Select(self.findElement(*self.articleType_loc)).select_by_visible_text(articleType)

    def typeComeFromAddress(self, comeFromAddress):
        self.findElement(*self.comeFromAddress_loc).send_keys(comeFromAddress)

    def typeCmsInfo_author(self, cmsInfo_author):
        self.findElement(*self.CmsInfo_author_loc).send_keys(cmsInfo_author)

    def typeAuthorOrg(self, authorOrg):
        self.findElement(*self.authorOrg_loc).send_keys(authorOrg)

    def typeIsTop(self, isTop):
        self.findElement(*self.isTop_loc).send_keys(isTop)

    def typeCmsInfo_issueDate(self, cmsInfo_issueDate):
        self.findElement(*self.CmsInfo_issueDate_loc).send_keys(cmsInfo_issueDate)

    def typeUploadify(self, uploadify):
        self.findElement(*self.uploadify_loc).send_keys(uploadify)

    def typeInfoContent(self, infoContent):
        ifram1 = self.findElement(By.ID, 'ueditor_0')
        self.switch_to_frame(ifram1)
        yy = self.findElement(By.XPATH, "/html/body")
        yy.send_keys(infoContent)

    @property
    def chickArticle(self):
        self.findElement(*self.chickArticle_loc).click()

    def getTitleName(self):
        return self.findElement(*self.infoTitle_loc).get_attribute('value')

    # def article(self, channel, infoTitle, comeFrom, articleType, comeFromAddress, cmsInfo_author, authorOrg, isTop,
    # cmsInfo_issueDate, uploadify, infoContent):
    def article(self, infoTitle, comeFrom, comeFromAddress, cmsInfo_author, infoContent):
        ''' 创建文章  '''
        self.chickCMS
        self.chickManage
        self.switch_to_frame(self.findElement(By.XPATH, '//*[@id="iframe_box"]/div[2]/iframe'))
        self.chickArticleAdd
        self.driver.switch_to.default_content()
        self.switch_to_frame(self.findElement(By.CSS_SELECTOR, 'iframe[src="/private/cmsUpdate/addInfoWeb"]'))
        self.typeChannel()
        self.typeInfoTitle(infoTitle)
        name = self.getTitleName()
        self.typeComeFrom(comeFrom)
        # self.typeArticleType(articleType)
        self.typeComeFromAddress(comeFromAddress)
        self.typeCmsInfo_author(cmsInfo_author)
        # self.typeAuthorOrg(authorOrg)
        # self.typeIsTop(isTop)
        # self.typeCmsInfo_issueDate(cmsInfo_issueDate)
        # self.typeUploadify(uploadify)
        self.typeInfoContent(infoContent)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.findElement(By.CSS_SELECTOR, 'iframe[src="/private/cmsUpdate/addInfoWeb"]'))
        self.chickArticle
        return name

    ''' 文章列表 '''
    # 导航栏cms管理元素
    CMS_loc = (By.LINK_TEXT, 'cms管理')
    # 导航栏文章管理元素
    manage_loc = (By.ID, 'infoManage')
    # 新增元素
    article_add_loc = (By.LINK_TEXT, '新增')
    # 查询元素文章标题
    title_loc = (By.ID, 'infoTitle')
    # 查询元素栏目
    channelId_loc = (By.ID, 'channelId')
    # 查找按钮元素
    check_Btn_loc = (By.XPATH, '/html/body/div/div[1]/button')
    # 批量删除元素
    deleteMutiInfo_loc = (By.LINK_TEXT, '批量删除')

    # 编辑元素

    # 删除 元素

    @property
    def chickCMS(self):
        self.findElement(*self.CMS_loc).click()

    @property
    def chickManage(self):
        self.findElement(*self.manage_loc).click()

    @property
    def chickArticleAdd(self):
        self.findElement(*self.article_add_loc).click()

    @property
    def checkButton(self):
        self.findElement(*self.check_Btn_loc).click()

    def checkArticle(self, title):
        self.chickCMS
        self.chickManage
        # self.driver.switch_to.default_content()
        self.switch_to_frame(self.findElement(By.XPATH, '//*[@id="iframe_box"]/div[2]/iframe'))
        self.findElement(*self.title_loc).send_keys(title)
        time.sleep(3)
        self.checkButton
        # self.driver.implicitly_wait(3)
