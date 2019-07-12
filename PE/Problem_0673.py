# At Euler University, each of the n students (numbered
# from 1 to n) occupies a bed in the dormitory and uses
# a desk in the classroom.
# Some of the beds are in private rooms which a student
# occupies alone, while the others are in double rooms
# occupied by two students as roommates. Similarly, each
# desk is either a single desk for the sole use of one
# student, or a twin desk at which two students sit
# together as desk partners.
# We represent the bed and desk sharing arrangements each
# by a list of pairs of student numbers. For example,
#    with n = 4, if (2, 3) represents the bed pairing and
#    (1, 3) (2, 4) the desk pairing, then students 2 and 3
#    are roommates while 1 and 4 have single rooms, and
#    students 1 and 3 are desk partners, as are students 2 and 4.
# The new chancellor of the university decides to change
# the organisation of beds and desks:
# he will choose a permutation \sigma of the numbers 1, 2, ..., n
# and each student k will be given both the bed and the
# desk formerly occupied by student number \sigma(k).
# The students agree to this change, under the conditions that:
#    1. Any two students currently sharing a room will still be roommates.
#    2. Any two students currently sharing a desk will still be desk partners.
# The downloadable text files beds.txt and desks.txt
# contain pairings for n = 500. Each pairing is written
# on its own line, with the student numbers of the two
# roommates (or desk partners) separated with a comma.
# With these pairings, find the number of permutations
# that satisfy the students' conditions.
# Give your answer modulo 999999937.
# ----------------------------------------------------
# Analysis: disjoint set union

66b62ae7d883540f16439ffb4c6f8952ac0e5b400e7fdab8a92740c5374313e243f79e70d51a8c43007798289b716890970bf54a8022b78756d84e70fc92a385afd17b439f8a8522cb03603c109e5d5802da627793fbf011731e157219c19ecaa7e3942d2fd2ccd7aa6b78ff8adc090ad739dd7d7248602a547fafec181455694f08ace58a9ad8ef750b233c4c6ce6bfaf15c46d5d72bee8c8a745fce57f412baf6d919069b5a3e338932e6eadf17ff29f8948095ffdf62786ee5f11abb72bb347eecc070c9e35222191b77aa3076cdd5757d8c60ce17d1c7971c6737d0e90a7ef5726c3204afbbb0aee60717680cb4c37ac657bffa12c1a059fe13a4d38cd527c2d2d7c1c4ad83f4c01bf14779d008799e7f4ebbc128e560c8ee7ce8cd412618afcc865eead568ee534a0cd1f664760a3450b19354eec09645d62ba2ce2d472c6b3becaf8216bdc171bebf87ffbf891254cdd87c45150a02200c16c1120ff38a4de285fe2d9c994b23c0f1e71cdd2ac3b0a62806d0e4e221963804e865c3e6d8a6e1fc6760b1269c0596d4713b16a4a0dafe92a182b72129242ead0c14bfcfea8083834b4f8ff310cbcce59e40d24b7729173fb7a60c8621831459573027ef3ac3bad59aa29f00b7cb5fe63530ec47ffc767c0fc9056bff86cbe6bdb1b1a9e4ab8db61022298184f33a1d60fdc4a522c5b5e7ab9b7709e6d0ed970c17a388304e21d1987c2d2d7c429c60a5acd487763ce0f3630cb416ac74c777487d6acaa8d8de8dab76d7577419839769f704cda78878533c3a42d08c229d2104f8c8c3890710087ecf78d557f52c23b442a897341383b58bcf5301eae95ff2ac5778d677c2938f07b79ed9b807bf4f93f5e5626759cf6d7fdd015436694ddfacbb607e989f68bb93385562ab4d221f1a27ebb364e226fdb6d941ff4e642f72574abd0957acbcfda74bb44e92ed28472bfd9277641bca2c7270b0e9610f3977b9ab37087a5a03dfce2bba8bafb381aa8cebc2eb95b940758e69b37fcfa7ca281c98d61a3c2cd9a69fd2b10d8f1596062b5a979178ce4f27b57a97b2a4201bf0da74857aa449fe616b6f1231177c2d2d7c258a7e42a998e8c1be1320353416731e7e50cb808385a6da5f46c0671dd1b5fb93a8cb544b4baf240a244443a049be4569b33afc43e368d5cc4b2f1c3a187c793558dbf15f4c084d212617c5c9cdb2ddc253d3a0d8168db477e4d43ff0b55031fc06bf74729f26834e834bf0eaf59d253bc6a7c0a59dfe494e6873f52204e43c63c89b3a75adbe7113bb6b86d7d62c16e4c2b60008f635bc5fbbb5f9da1dafe8237fb3878bb529a61fb9177f56a23a63eb90ebf2e96bc35b975ec24af99b805adda4ff75f770f89ebf863ef79088e7ae85294a248e948c5cc8c43553111ca040e194879e5f0e690db6e6619c2674a7e7aff8c5396023a8a7664f505476ca9e0b7c2d2d7c09df6585826701cf2cdf190ff02bbc020b3ea073cf77ba1efd579a3bcf0c8d30830c2e64b634d26a6ecdca9b82b3f286e263221072aa7f468b42424258618c49123740bdff3db280bdd41c569063efcba2990bccaa06d9483495c9541f0030b4260949c6e8e1532f87e382dc07a76dc7b81c9a062dd587b2a889c6875620354f9db311af7ae5701c194b4dc8c4851fb9a8f36c5ca6803ddbdc62d0057b936e55766d69335327539485ed1fc2d85abff27e3b74c8398a09a01d932c37e88e3b0d86ab0abbb5665b6873e2c056b7066e376d8cb4ebef408266028162e534b67d4bb1c16c31d7b3bddef30d7ec497fb9d7091105820968d5db8fdb8607140776ae27c2d2d7c5671b0f84f0b30425b37511b40a50e2eba8e4dc3c525672c317fe5c4ac1addbd4ab4f9a3194d2e4190dc513df67412b95fc78f688bfdace71372660b84fe901b38728755da208805832363013c9322d4be5c00d2809b0e6114120c2efb36c16a3b3011f972771bd087ce04ce257b6323e99b1d2802ae0496160f60d4c8714377d58f747e0d1e4c8e7d472c4b95a4dd1997650c0a65e604a348d31e135c5a5e2273bc43bdb5170dcd841ce3db1fcacd8ebe4b762d35c915511257d49f78800ca0a75e05b7fdde8362105e52beb4c2caed5cc7376fdc040b6b5d45d0f89cf5b3a65f1b6a7553f9f44b19eb15bb463449aef8b3017f92a51e0943e3e4c478c7bdbd7c2d2d7cc869276e3280731c41ff57948730e0311ecc0b44e167f9baf44433d8b6968ce63bc59a7867c1ac0ba23a834b3fff6c20e1504c460acdcc362516a99128742d54bdc4868db96c13eb613e364b762fd5c7e30f2dee80d76f110b08a5a025ab415f4eb13d62f3bec14d5fa15bd4d663e8665d32fd8228181ea64b0a68028030f84f34df4449214a9de86d6d99242ff6b83fcc690c5d7e4476c2f42e66bfe5b1d19868f2969428977fec6ca9e386814ffeef55d1a3fa8f744fffe1b40ce8198fc68668dfbc5b478cbc4c4fa254a5a4be9fc66cff6d3b9e46979e49967a764c80cd890f795a03905de290bebb59e132e4ad4196e08dd8df598750005d0748d9aa6b187c2d2d7ca50d8d8dc59dc20f1b25905628c7032fa0185ad20f175e962a9d89cb209c47092d11f64a24d00e4d6fe4e2c3f683d93c895caf2b0da935791aca137e48e1c6f26d0598bd8b52e242720a23773d147d9fce8377b80b2ce5114bc4376fc0a6c57a8667414926af35e88b64833de13059041366cf7270dcfe2ee566c293019709938ca449f4f35bea90f9b493aabbd22c7de64db718815b8c88645f5095dec89a3b6b6990f7c0b10cb06815bfe35302588d32339e559fc1d51942c6443c67fd575a1a374f4d7e926bedeb396d25b0e65166d45aababff129aff99cca8be01b73aee63a5277b4e467ebd73b4b978958839250d4a72b50569999f48c60f4bc47185e6
