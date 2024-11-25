function Main0()
    -- 直接修改数值为 500
    modifyValue(500)
end

function modifyValue(n)
    -- 清除
    gg.clearResults()
    gg.setRanges(32)
    
    -- 第一次搜索
    gg.searchNumber("0.0001E;1E::30", gg.TYPE_DOUBLE, false, gg.SIGN_EQUAL, 0, -1, 0)
    gg.refineNumber("1", gg.TYPE_DOUBLE, false, gg.SIGN_EQUAL, 0, -1, 0)
    
    -- 获取结果数量
    results = gg.getResultCount()
    
    -- 判断
    if results < 8 then
        -- 清除
        gg.clearResults()
        gg.setRanges(32)
        
        -- 第二次搜索
        gg.searchNumber("0.0001E;1D::30", gg.TYPE_DWORD, false, gg.SIGN_EQUAL, 0, -1)
        gg.refineNumber("1", gg.TYPE_DWORD, false, gg.SIGN_EQUAL, 0, -1)
        
        -- 第二次搜索结果修改
        gg.getResults(8)
        gg.editAll(n, gg.TYPE_DWORD)
    else
        -- 第一次搜索结果修改
        gg.getResults(8)
        gg.editAll(n, gg.TYPE_DOUBLE)
    end
    
    -- 清除
    gg.clearResults()
    gg.toast("修改成功")
end

Main0()
