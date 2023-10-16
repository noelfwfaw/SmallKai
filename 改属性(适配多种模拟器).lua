function string.split(s, p)
    local Result= {}
    string.gsub(s, '[^'..p..']+', function(w) table.insert(Result, w) end)
    return Result
end
-- 199034;6;3:60>-100;417>-100
-- {Id};{Star};{Type}:{Attribute}>{Target}[;{Attribute}>{Target}...][|{Id};{Star};{Type}:{Attribute}>{Target}[;{Attribute}>{Target}...]]
function ChangeShipAttribute()
    local Result = gg.prompt({"格式：{舰船Id};{舰船星级};{类型Id}:{属性}>{目标值}[;{属性}>{目标值}...]，多个之间用'|'连接"}
			 		    	,{}
			 		    	,{"text"})

	local TargetList = string.split(tostring(Result[1]), "|")
	local OriginalRange = gg.getRanges()
	gg.setRanges(gg.REGION_JAVA_HEAP
			 | gg.REGION_C_DATA
			 | gg.REGION_ANONYMOUS
			 | gg.REGION_JAVA
			 | gg.REGION_STACK
			 | gg.REGION_ASHMEM
			 | gg.REGION_OTHER)
    for i = 1, #TargetList do
        local SplitedTarget = string.split(TargetList[i], ":")
        local ShipData = SplitedTarget[1]  -- {Id};{Star};{Type}
        local ShipAttributeList = string.split(SplitedTarget[2], ";")
		--[[
		{
		{Attribute}>{Target},
		{Attribute}>{Target},
		...
		}
		--]]

		gg.searchNumber(ShipData.."::610", gg.TYPE_DOUBLE)
		gg.refineNumber(string.split(ShipData, ";")[1], gg.TYPE_DOUBLE)

		local SearchResult = gg.getResults(1024)

		if next(SearchResult) == nil then
			gg.searchNumber(ShipData.."::610", gg.TYPE_DWORD)
			gg.refineNumber(string.split(ShipData, ";")[1], gg.TYPE_DWORD)
			SearchResult = gg.getResults(1024)
		end

		for j = 1, #SearchResult do
			local MemoryFrom = SearchResult[j].address - 0x1850
			local MemoryTo = SearchResult[j].address
			--[[
			Here, I have tried my best to find out the memory range of ship's attribute which is relative to ship's id.
			And I have tested this range on local android simulator and on cloud phone.
			The upper bound is 0x1850 which will cause game crash and fail to enter a battle in opsi and main if you set
			upper bound greater than this, and in most cases, ship's attribute is modified correctly.
			But in some cases, the ship's data such as its attribute can't be searched.
			I truly don't know why.(Maybe dynamic loading causes this?)
			Maybe I am a noob. :)
			--]]
			for k = 1, #ShipAttributeList do
				-- fuck gg
				-- fuck lua
				-- fuck dynamic type
				-- fuck everything
				local SplitedAttribute = string.split(tostring(ShipAttributeList[k]), ">")
				local AttributeToSearchList = SplitedAttribute[1]
				local TargetAttributeList = SplitedAttribute[2]
				gg.clearResults()
				gg.searchNumber(AttributeToSearchList, gg.TYPE_DOUBLE, false, gg.SIGN_EQUAL, MemoryFrom, MemoryTo)
				local AttributeResult = gg.getResults(1024)
				if next(AttributeResult) == nil then
					gg.clearResults()
					gg.searchNumber(AttributeToSearchList, gg.TYPE_DWORD, false, gg.SIGN_EQUAL, MemoryFrom, MemoryTo)
					gg.getResults(1024)
					gg.editAll(TargetAttributeList, gg.TYPE_DWORD)
				else
					gg.editAll(TargetAttributeList, gg.TYPE_DOUBLE)
				end
				gg.clearResults()
			end
		end
    end
	gg.setRanges(OriginalRange)
	Exit("修改成功！")
end

function Exit(Message)
    gg.alert(Message)
	os.exit()
end

function Main()
	Choice = gg.choice({
        "改属性",
		"退出",
	}, nil, nil)
	if Choice == 1 then
		ChangeShipAttribute()
	end
	if Choice == 2 then
		Exit("退出成功！")
	end
	FX=false
end

gg.clearResults()
Main()