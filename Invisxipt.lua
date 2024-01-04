local character = game:GetService("Players").LocalPlayer.Character
local humanoid_root = character.HumanoidRootPart
local old_cframe = humanoid_root.CFrame
local new_root = character.LowerTorso.Root:Clone()

humanoid_root.Parent = workspace
character:MoveTo(Vector3.new(old_cframe.X, math.huge, old_cframe.Z))
humanoid_root.Parent = character
task.wait(0.5)
new_root.Parent = character.LowerTorso
humanoid_root.CFrame = old_cframe
