function Main()
    gg.clearResults()
    gg.setRanges(32)
    gg.searchNumber("0.0001E;1D::30", gg.TYPE_DWORD, false, gg.SIGN_EQUAL, 0, -1)
    gg.searchNumber("1D", gg.TYPE_DWORD, false, gg.SIGN_EQUAL, 0, -1)
    gg.getResults(100)
    gg.editAll("500", gg.TYPE_DWORD)
    gg.clearResults()
    gg.alert("修改成功：已将倍数设置为500")
end

function exit()
    gg.alert("退出成功")
    os.exit()
end

while true do
    if gg.isVisible(true) then
        gg.setVisible(false)
        Main()
    end
end
