# Sam and Max are asked to transform two digital clocks
# into two "digital root" clocks.
# A digital root clock is a digital clock that calculates
# digital roots step by step.
# When a clock is fed a number, it will show it and then
# it will start the calculation, showing all the intermediate
# values until it gets to the result.
# For example, if the clock is fed the number 137, it
# will show: "137" -> "11" -> "2" and then it will go
# black, waiting for the next number.
# Every digital number consists of some light segments:
# three horizontal (top, middle, bottom) and four vertical
# (top-left, top-right, bottom-left, bottom-right).
# The clocks consume energy only when segments are turned on/off.
# Sam and Max built two different clocks.
# Sam's clock is fed e.g. number 137: the clock shows "137",
# then the panel is turned off, then the next number ("11")
# is turned on, then the panel is turned off again and
# finally the last number ("2") is turned on and, after
# some time, off.
# Max's clock works differently. Instead of turning off
# the whole panel, it is smart enough to turn off only
# those segments that won't be needed for the next number.
# The two clocks are fed all the prime numbers between
# A = 10^{7} and B = 2 \times 10^{7}.
# Find the difference between the total number of transitions
# needed by Sam's clock and that needed by Max's one.
# ----------------------------------------------------
# Analysis: brute force
#            ---0---
#           |       |
#           1       2
#           |       |
#            ---3---
#           |       |
#           4       5
#           |       |
#            ---6---

169adf3c96ef9ee07a0716b11367b7e41379892be143235cbf4f7292172413c97ca6b411f3cc7bb4ff6e32c08c80706ad3deb6c413da452e0c249ba1630e6fc39359441541d384a309f78e0ab2fb1d53dd2cd73044ec6fbe870338107c6a12ded3f2388867d164396c62b8aa5c5aeffc610999570f1df14dafd0264189bbd02040c36dab6eae640e3a0413fe70157575d8070958e8ce8717b3a33d5c7a57e4f8be77049fc0596e1ed8a17cad0e0870744ea7eae84742b785d98ebbe4c243745e62a48aa1a311d3fcb627f2416ac771183a45686edbdde39465416d9ccf02ab7ba06d8e57232e2d3b268425a1570347b9654772f80573153d51ae4b45c34b29ba7c2d2d7c1b1ce8eef1c4dfcbb95ac68839ffdef430e38da5e8ea8bf4a4af1ddc5ead9744306879eeaa1c48c69d0e2cffe4b9d657ad323a71252b85878b071854f13e84fa89d071eaa1e0c16656cf34e589c32d51d9cae0c6abdfb4c64b0e52ecfbd5be20de7e6b2829fcc1a8c56bab5b1b536e0cb87db01441cd95ec5e75aae7badf70358c1e93cf4190726bdeb57b9881013e97648effab51b69eddb9525a64a77c922bba41b06f538ee36bd9af63a13feaba5356ba4525a29340fd41a538950115a39b90ea3947ec7aa27ce31db176d66b95a489a62a9d251097d790d5ee4e56ce9661b979b26e75c524a9fe7302cf364b2eddac231d72447f1ebb717804689b45f44f7c2d2d7c0d125259e53dda8c074f37feae901153caf2a60092806141804448d80bcc56696af66c8e6ddeb2f4b73c8081bc4be32a6fcfafa0589f46adca61a5f58556da1bb6affba42a831fd397d1767cb5ec1ac8c28353b0dae220ad4432041f05658c85fdba0295efefc4a64c6ec0c4ff83d87e0f319bf95975f828ab5f1456f6dc1c0362f325341f09e36d1a4440e5828b10e5b41ed2348bb31dc9f73f032f43ca1b47e38c7a79d7b13e0aef8e9379d1b8d349b3056b8c9bb1118e9e920bd364a5a5db65be4850a05c6d401fe54445348e05d2d80b28c5a06dc7076cf4bd1b846643a2f9e25421b66a016e99380c6af2450fec64330e9f237fed159b255c9077658e3c7c2d2d7c0688b8f76bc03573f29b6a13f1ddcc0373807914b7a2cfb2f603eb36e3b43a68fc30b24f7e0e343c7eb5dde662ea740fe49a4989716ed4f99fd2806049e9f85d7fef64fcf9f894f0cb4d5749f5de29313283aff02f94f6bfea63226a687b1aa9de988b9a2d7a3d852ca6833000d71808ca13045742f5fe5da95509676f42e9c031071b5514bb9f4e84071c2c99c8ece0d9b01e56dd3ce15f71aa94ffa068bbb62d7691347a466d4bfc2e7b523cbaa92024a1138edb459a5046f606049f9868b110c01fe5cb1d691191e4fce2f9f399aadbb2bc40538034ba46079aab4e764412a6c1d1b9c6e8057c52c86a47ae0889768dba56b9de1e0d98e9c9b174f45b429a7c2d2d7cc87f56e5182ac1a77c547638bd5a25e72b5fd33a29d940db5a1d9165be88e5b105199595b5d939f58bd719cc0f536bdbaf126573a4bec4e37ceaef1cdc72ac5444515bc40c883e63599c78a843b09a8e69c544720743be1c323fac67cbf273ff95145cffc86cbda6119fbee86201e6505c6933db1ae5765d34eae65fda1e196c84660909a07852e6ffe3c924860673745c088c8b67fa85ee56bada958b50eaf101902416c4b12cda3e5a23beb0c44ca136bfc665c181c65fec1349ba917e08e8ff159d54a9ab039dc59f23c90d76036779f001ad2555512db735623eae6b8df8c05a2c692601b45d6b49701493cd4f3fee8e1ed1934d90891a2f82d3ad4be9457c2d2d7c068fee80b0692a7bfe9853e58a31b822aa09f0b81296fbd551818300c6c65f512e5bf076393a8dc7a7c0c5c11bcdd030d95dd1da971b7048c1136e9d29adfe4dd6203e749df8f79714b0058a163e0c23c95f3f9ace8373ed902a92c8f4fd631e2bffc45645c3b5af34f543fecaa62d8a2bf01de75a3dad5fded9896cbc5a65540d962a9a7f529fa8cdc0c034e02392986b858d58f5517278423da1fda112e415d96c6d907d8211e73bfa1efcc9b24f43e0218fe236f40741648882450b5c38ab8ae35b9f2e2c45e61910819f9a86100fecb26643c45187f5cd350a3c4bf48904b5df5e062c9e1957f7835cd2a8759259db29cbf4b13d12b80792ab298f06d35f7c2d2d7cc236c4371f5a3e7a8acbf1f2db1ecc61a087ac071acc1cb22a56fd18bfd6f5dff732f785c591846c984338ee26efc359c4597a9386626a5083c85267c690672d06e060e2bb111d944b3341c0af560cb9af12131e3da1ad4e03e44777374b2aabf1dd0b2930718b4994181df8f86ed35157fdf4c4c609350b58dbfe0c187c076958434d269da5682c5904fd68994b339a72c332fd7eceaf35e117fc23ec2727f962e9f7fd1a8460013cbc7f704fdd6e0a135c3c8f03f3e09f29512aed51d7ab06109ee96d508ea04face7f69e666685edca23442e97996e70df4075664b18b9c0c240f4c36156df584a5642fe0ccf1f863bd5abfba93a2f6c5a246a00931f7a48
