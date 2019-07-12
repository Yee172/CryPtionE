# Let T(n, m) be the number of m-tuples of positive
# integers such that the sum of any two neighbouring
# elements of the tuple is \leq n.
# Find T(5000, 1e12) mod 1000000007.
# ----------------------------------------------------
# Analysis: Berlekamp-Massey Algorithm
#           Let D(t, m) be the number of m-tuples of positive integers start with t, we get
#              D(1, m) = D(1, m - 1) + \cdots + D(n - 4, m - 1) + D(n - 3, m - 1) + D(n - 2, m - 1)
#              D(2, m) = D(1, m - 1) + \cdots + D(n - 4, m - 1) + D(n - 3, m - 1)
#              D(3, m) = D(1, m - 1) + \cdots + D(n - 4, m - 1)
#              \vdots
#              D(n - 2, m) = D(1, m)
#           Then we have 
#              T(n, m) = D(1, m) + D(2, m) + D(3, m) + \cdots + D(n - 2, m)
#                      = (n - 2)D(1, m - 1) + (n - 3)D(2, m - 1) + \cdots + D(n - 2, m - 1)
#           Keep doing this process, we can see that this follows the prefix sum similar property
#           Let A = \left [ \begin{matrix}
#                           1, 1, 1, \ldots, 1, 1
#                           1, 1, 1, \ldots, 1, 0
#                           \vdots, \vdots, \vdots, \ddots, \vdots, \vdots
#                           1, 1, 0, \ldots, 0, 0
#                           1, 0, 0, \ldots, 0, 0
#                   \end{matrix} \right ]
#           be a (n - 1) \times (n - 1) matrix,
#           then the element at the upper left corner of (A ** (m + 1)) is the answer
#           However, the time complicity is O(n^{3} \log(m)), which would be large when n = 5000
#           Thus, Berlekamp-Massey Algorithm would be implemented to reduce time complicity into O(n^{2} \log(m))
#           By the way, using PyPy3 will be much faster.

75b3e1c4654001a29fbceaa4743928d328ad6ac7f58fdb5e7ff955625afdc735670eff0675d11ee3186a0eb08b9ea73ad09e54065cabc00193cbaf13cec3bcbdc32410b1b7b444b662d8cc2e2622be44d284c909dd50c2bbdcefafa27c2d64372b7fee697770dca6b2fb57aad7f8654313c27e481a090b06e167de5fc774c6aa8e6e8ec7b5e3a111750c3672b12846c8ea5e948378845735976c275b19453a371af15df4f5f265bb4621a287e5daaf1baaa06d8885f815d9593169bd556341df958678aad53c0f8a2da1ad4fef1a9a11de01349ba828a2c3d9e553d0586a76f8390113a9f21cda6944ad619c8d2653a67605c05ce83ee0447392cf152e99eba97c2d2d7c7b04b7f700026a7ba5be892ce560c8fe9e2d8128452829caaf5f135e2431507fdf44bc6c2841c7877a931c115ba8d44c9053e23f8ad473a50336979698d9538fa66e2d2d43c9c5692f7abf42e7cb3ba4ddc17c6882dd10576c5d2c5d61573f8c4cefe7d341d2d2da7af58237cc43cc2fee532e162cba37d8720abe2d128e6e94d6944ac1582072ed3826515436d8cd92bf063818a61e3342bf123e64dd3b8ab6af5ecfc984629881c2a1c0e6a9c689e1a2c8ad04e696ba4f54ffd288f211f73d4c446a2870924c124d123bf960af7ec38bbc88ec4eb2beff5028e04ec2c1614164a0fd33e4b4a0dde428b208add82662dcc827f49309ee27359280d8ad5182157c2d2d7c869d0441ce7555a1160fd850e574d28fe8c98c355aaba6223c7c82a022907e1aa39d4bb6cb8c2be1aa85ea1a2dd3a33dfe77db90547dbd550fe3c82f419cbe2ce5d783ff7105719bf1bf83336b84f494b42c8419ab57bd5aae072f4a1444848ec4395527cb080063ed053d871bf7d31e4d5b5cc351e983dee210f730e2e70d47bb06f2524c41b5f88de0fcd98beab8ad61372177ea7425c61f7d1646c77429574fe0e493f36a988a0310a60690f670b8d574e1a52b8d42b059286c11dcb8f622211c2647e1ebb3b89c720fdda1c07f26f29eb32ae571494b9a5da8aa36bb7c097263bbe14f738c5db93b8e7246f28c5ad7fb0439ac118f872845ae9e11505bf17c2d2d7c2b29222affae271b9f6994ef71c5ae83d7a2c384510d203cc30e779d29b82a3941d6b4751de70bb06824ee95b21479fed135a9b8b6934381417f6de7684713737c9ba37de04e4c62d9e4c7e4b67be7010206c75bf3532282646cb4e79fe074c2c1dbcd93446096f28e020510a56bddb3c13728217c2123ed47ffcc81683d74e001691e0d70b1a5ef12abdfd78440e232be64a07bbdb218be622ea1d8431a48b12664c5b39c5ef884d6e43b20ed1e78629aac48f45096cc37cc0839de341933fe4b302b5b66a0d7911f7d34d942865caf4c6e71a9afc330554ba3a6e2a6766c6961b6905425750583068d89603d5ddb8fcc2249a122484e96aedd4fc81a2bd597
