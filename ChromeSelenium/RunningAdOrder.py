from WebFroxy import WebFroxy

def doOrder():
    try:
        loginBtnLinkText = 'ログイン'
        idInputTxtName = 'id'
        inputId =  'kakakzkz@naver.com'
        pwInputTxtName = 'password'
        inputPw = '1111'
        loginSubmitBtnId = 'loginSubmit'
        directOrderBtnLinkText = '簡単！価格検索・注文'
        insertCartBtnId = 'cart-bottom-btn-reg'
        orderBtnId = 'cart-bottom-reg'
        payTypeSeletFrexBtnId = 'rbPayment8'
        payBtnId = 'orderEnd' 
        confirmSubmitBtnCssSelector = '#confirmButtons > .o'
        mypageBtnLinkText = 'マイページへ'

        wf = WebFroxy()
        wf.openBrowser('http://77.local.adprint.jp')
        wf.doClickByLinkText(loginBtnLinkText)
        wf.setValueByName(idInputTxtName, inputId)
        wf.setValueByName(pwInputTxtName, inputPw)
        wf.doClickById(loginSubmitBtnId)
        wf.doClickByLinkText(directOrderBtnLinkText)
        wf.doClickById(insertCartBtnId)
        wf.doClickById(orderBtnId)
        wf.doClickById(payTypeSeletFrexBtnId)
        wf.doClickById(payBtnId)
        wf.doVisibilityClickByCssSelector(confirmSubmitBtnCssSelector)
        wf.doClickByLinkText(mypageBtnLinkText)
        wf.quit()
    finally :
        wf.quit()

doOrder()