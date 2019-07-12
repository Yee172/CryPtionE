# In the game of darts a player throws three darts at
# a target board which is split into twenty equal sized
# sections numbered one to twenty.
# The score of a dart is determined by the number of the
# region that the dart lands in. A dart landing outside
# the red/green outer ring scores zero. The black and
# cream regions inside this ring represent single scores.
# However, the red/green outer ring and middle ring score
# double and treble scores respectively.
# At the centre of the board are two concentric circles
# called the bull region, or bulls-eye. The outer bull
# is worth 25 points and the inner bull is a double,
# worth 50 points.
# There are many variations of rules but in the most
# popular game the players will begin with a score 301
# or 501 and the first player to reduce their running
# total to zero is a winner. However, it is normal to
# play a "doubles out" system, which means that the player
# must land a double (including the double bulls-eye at
# the centre of the board) on their final dart to win;
# any other dart that would reduce their running total
# to one or lower means the score for that set of three
# darts is "bust".
# When a player is able to finish on their current score
# it is called a "checkout" and the highest checkout is
# 170: T20 T20 D25 (two treble 20s and double bull).
# Note that D1 D2 is considered different to D2 D1 as
# they finish on different doubles. However, the combination
# S1 T1 D1 is considered the same as T1 S1 D1.
# In addition we shall not include misses in considering
# combinations; for example, D3 is the same as 0 D3 and 0 0 D3.
# How many distinct ways can a player checkout with a
# score less than 100?
# ----------------------------------------------------
# Analysis: brute force

6ee3f0ea2e5edc6137913793f6cf21c263a63511d4ebce7a2df2591594bc8d144c349fa1bef7ee7158409778f80d9228c7c7f56313637be7756045b2e6e15fcf999c7cf27f8f88896dd22daad9cc2b7f1b3a746bacfa389762bf16f879f0d2b3b0b342f40573995eff0100bc057c24d89c616b87f51ba4df286f05967ef0fa93c39cdb12562d7876ecadae78ab3e858db6740b02a1b50807e214e2b77627001cc27310d4697d0ebfafe5286cd7d5ded5de7660ef806518b4e1690a301801d62a3f3679c79a59e147be22f419a5deb9897ef2cd042f59b0d073213dac8e5e3da7196d820528757609238dc6464194a192a7ee5b5e7aad96946c5ce6de0df55b217c2d2d7c8822401d50140034153eea0ba86a8d2e7bed685ceca8618456aaea909c96016210aa6b06da641da5fdfc53b1c9ffac7003f7ea3e141d2280f1b10843766d2aa2822594ffb4c06bc5260d10d3d1b32533cedc8dac8f282dec22210351dec5de7b867b1a1207ff5194c3781c73e2316e775061699dbde0192af3bfe58a692c01abca8444b2e47a866959b3220bb4fc4f8da3e5d11db24e5dbedb6dd7775f8d7d4256c13c7e456df8573345f735e405e06186f548a5a57763b0b6b1a10186cbcb0dd05a78b3dee9b578d1234f7fbe47203fb05c0ecb79f1e5d3d4dba5c95e0818639ed924fa434ab2958f0a3ce022b6974d4c13043def8444bd98d127057b2dc0047c2d2d7c36aa73eb1f300e473391523b5e78cc554383b89a59ca770ee8d8727b709d8491a3af901ccdae3232085b161b6fae11b074365a8a43d96b57f78a68716e90b5aaed5d3158fc559ec1e1cf52cae06f41023a46a511a6ab3aa407027ef8fb1106d0c31363dcc361677862d35c683f3fd972b8b4f6929fb89c695680310fe453105dec0df34dbdb5f9925342824d1c88aa2e7bbd07999b8973ea5df6dc08d9f2fb4438562312ba0de9e18d5aff6c2d35e5d5e0fb47b3b790a94d872e51729302c87ec20d3d072a5c3cf702414d9f9f0beb3359d8392ad24845e2a8f3bbf6ece389ef8c218782ddfafc5051490b2b554e78ed33904618ce83f0adea8044f3bec442797c2d2d7c0ba701c121a1bae2e8fa631bdfc704b59c458ec4e76fb1ae7b77d121224f1a62bbb474135820e1fba8bccac77c25ca23f08983040716225fdc8e103dec25a9314f2dd77b5b01156a2f2a870c927bb586c99a3477577bf84d0001d1a937cda6f0395009d22422f8259697c63dcedf1b83e37cbf7ce08f94140c2c65702a464867be4bed0a8c0d6892346ff9979efadd0f0db007fc3f755dfe9521d80bf3e47c4003eedf89ef0a2866bf740732beaab972286c24621367ed993b11d7c4a8e0f26288ad1228f3479f3781a953ac69feab0096a8e81caa6cf2c7d24f73305736669226e335f19568bc6503f9608c540ea3ac46a7315c2ab5316bc27ae00767da0a0c7c2d2d7c1a69c05bbfd7c8cebf4815c608441359f52da05332bc3953269b3dec7b80fb5fb69c8cc78b080cabbb8e3a33dcddbe19e167d0224eaba5155f428131641cd1134cd82328c2f70f18d0f457f15132de3be0b53b887899c44b58af737fde809663e6b8d034db08b6bdc76c717f024650599c1e8f3c162997e6aad93944ccae249db70bc7461a917be96c3e215bd936199bf11a425f05942e4dd2526ca0b97d7b20b3d3a058cf716bd3c3f86a229606ed6e28d0758deb40f04e454b5ad3c6ab82bf7bbcf47f2a7129604a0bb7e263ccf134a4df8cbd635c7e81ae86178e1bc7d0d38f936665f5c93e6fb390238d9cbe6a1f0764f78473af2dc5cd52c5d179122119
