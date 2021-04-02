var maximumWealth = function (accounts) {
	let max = 0

	for (let i = 0; i < accounts.length; i++) {
		let accountValue = 0

		for (let j = 0; j < accounts[i].length; j++) {
			accountValue += accounts[i][j]
			if (accountValue > max) {
				max = accountValue
			}
		}
	}
	return max
}
