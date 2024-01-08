-- Universal Death Messages Script By Orange Wood#9779/Espon



local list = {}
local list2 = {}

--reactions can be changed
list[1] = "omg."
list[2] = "oof."
list[3] = "sad :("
list[4] = "better luck next time."
list[5] = "rip."
list[6] = "lol"

-- reasons can be changed
list2[1] = " died,"
list2[2] = " failed,"
list2[3] = " had a heart attack mid game,"
list2[4] = " unfortunately passed away from to much water,"
list2[5] = " got lost and couldn't find their mama,"
list2[6] = " needed therapy after that death,"
list2[7] = "'s mom found their 'homework' folder,"
list2[8] = " died, this isn't fortnite,"
list2[9] = " suffered a stroke,"
list2[10] = " forgot their not invincible,"
list2[11] = " lived a short life but they won't be remembered,"
list2[12] = " died a long life,"
list2[13] = " died of fearing the dark,"
list2[14] = " fell down the stairs,"
list2[15] = " couldn't get to the bathroom in time,"
list2[16] = " tried to fly,"
list2[17] = " forgot how to play,"
list2[18] = " forgot how to breathe,"
list2[19] = " choked,"
list2[20] = " tripped on air,"































































for i,player in pairs(game.Players:GetPlayers()) do
    player.CharacterRemoving:Connect(function()
        lis = {}
        lis[1] = player.Name
        lis[2] = player.DisplayName
        local args = {
            [1] = lis[math.random(1,2)] .. list2[math.random(1,20)] .. " " .. list[math.random(1, 5)],
            [2] = "All"
        }
        game:GetService("ReplicatedStorage").DefaultChatSystemChatEvents.SayMessageRequest:FireServer(unpack(args))   
    end)
end
game.Players.PlayerAdded:Connect(function(player)
    player.CharacterRemoving:Connect(function()
        lis = {}
        lis[1] = player.Name
        lis[2] = player.DisplayName
        local args = {
            [1] = lis[math.random(1,2)] .. list2[math.random(1,20)] .. " " .. list[math.random(1, 5)],
            [2] = "All"
        }
        game:GetService("ReplicatedStorage").DefaultChatSystemChatEvents.SayMessageRequest:FireServer(unpack(args))   
    end)
end)

print("Death Messages Enabled.")
