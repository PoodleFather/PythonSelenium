from WebFroxy import WebFroxy

class OrderProc():
    wf = WebFroxy()

    def doOrder(self):
        try:
            self.doAdOrder()
            self.doMkOrder()
    
        finally :
            self.wf.quit()

    def doAdOrder(self):
        loginBtnLinkText = 'ログイン'
        directOrderBtnLinkText = '簡単！価格検索・注文'
        insertCartBtnId = 'cart-bottom-btn-reg'
        orderBtnId = 'cart-bottom-reg'
        payTypeSeletFrexBtnId = 'rbPayment8'
        payBtnId = 'orderEnd' 
        confirmSubmitBtnCssSelector = '#confirmButtons > .o'
        mypageBtnLinkText = 'マイページへ'

        self.wf.openBrowser('http://77.local.adprint.jp')
        self.wf.doClickByLinkText(loginBtnLinkText)
        self.doLogin()
        self.wf.doClickByLinkText(directOrderBtnLinkText)
        self.wf.doClickById(insertCartBtnId)
        self.wf.doClickById(orderBtnId)
        self.wf.doClickById(payTypeSeletFrexBtnId)
        self.wf.doClickById(payBtnId)
        self.wf.doVisibilityClickByCssSelector(confirmSubmitBtnCssSelector)
        self.wf.doClickByLinkText(mypageBtnLinkText)

    def doMkOrder(self):
        self.wf.openBrowser('http://51.local.makumaku.jp')
        loginBtnClassName = 'function--login'
        goodsLinkClassName = 'icon-lc-IB-TO'
        priceTableClassName = 'salePrice--tb_price'
        afterMakeClassName = 'afterMake'
        fileTypeId = 'fileTypeDesignA'
        insertCartBtnId = 'buttonToCart'
        orderBtnId = 'buttonToOrder'
        saveDeliveryLinkCssSelector = '.saveDeliveryInfo'
        payTypeSeleteFrexCssSelector = '.frex'
        orderConfirmBtnId = 'OrderConfirmButton'
        layerPopupCloseBtnCssSelector = '.ui-icon-closethick'

        self.wf.doClickByClassName(loginBtnClassName)
        self.doLogin()
        self.wf.doClickByClassName(goodsLinkClassName)
        self.wf.doClickByClassName(priceTableClassName)
        self.wf.doClickByClassName(afterMakeClassName)
        self.wf.doClickById(fileTypeId)
        self.wf.doClickById(insertCartBtnId)
        self.wf.doClickById(orderBtnId)
        self.wf.doVisibilityClickByCssSelector(saveDeliveryLinkCssSelector)
        self.wf.doVisibilityClickByCssSelector(payTypeSeleteFrexCssSelector)
        self.wf.doClickById(orderConfirmBtnId)
        self.wf.doVisibilityClickByCssSelector(layerPopupCloseBtnCssSelector)

    def doLogin(self):
        idInputTxtName = 'id'
        inputId =  ''
        pwInputTxtName = 'password'
        inputPw = ''
        loginSubmitBtnId = 'loginSubmit'

        self.wf.setValueByName(idInputTxtName, inputId)
        self.wf.setValueByName(pwInputTxtName, inputPw)
        self.wf.doClickById(loginSubmitBtnId)
