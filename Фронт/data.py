ip = 'http://192.168.43.111:8545'


address = '0x72b93b883BF89bd80779a9E6Eb75234d55D96bBE'
abi = [
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "Name",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "FulPrice",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "Id",
				"type": "uint256"
			}
		],
		"name": "AddBasket",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_toaddr",
				"type": "address"
			}
		],
		"name": "AddNewAdmin",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "Name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "Description",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "Ingridients",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "Price",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "ItemId",
				"type": "uint256"
			}
		],
		"name": "AddNewItem1",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_toaddr",
				"type": "address"
			}
		],
		"name": "AddNewManager",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "login",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "pass",
				"type": "string"
			}
		],
		"name": "Auth",
		"outputs": [
			{
				"components": [
					{
						"internalType": "string[3]",
						"name": "Fio",
						"type": "string[3]"
					},
					{
						"internalType": "string",
						"name": "login",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "pass",
						"type": "string"
					},
					{
						"internalType": "enum name.Roles",
						"name": "Role",
						"type": "uint8"
					}
				],
				"internalType": "struct name.User",
				"name": "",
				"type": "tuple"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_Role",
				"type": "string"
			}
		],
		"name": "ChangeAdminToManagerOrUser",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "ChangeManagerToUser",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "FulPrice",
				"type": "uint256"
			}
		],
		"name": "FullPrice",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string[3]",
				"name": "Fio",
				"type": "string[3]"
			},
			{
				"internalType": "string",
				"name": "login",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "pass",
				"type": "string"
			}
		],
		"name": "Registr",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "ReturnBasket",
		"outputs": [
			{
				"components": [
					{
						"internalType": "string",
						"name": "Name",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "FulPrice",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "Id",
						"type": "uint256"
					}
				],
				"internalType": "struct name.Basket[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "ViewAllItems",
		"outputs": [
			{
				"components": [
					{
						"internalType": "string",
						"name": "Name",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "Description",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "Ingridients",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "Price",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "ItemId",
						"type": "uint256"
					}
				],
				"internalType": "struct name.Item[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "ViewLk",
		"outputs": [
			{
				"components": [
					{
						"internalType": "string[3]",
						"name": "Fio",
						"type": "string[3]"
					},
					{
						"internalType": "string",
						"name": "login",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "pass",
						"type": "string"
					},
					{
						"internalType": "enum name.Roles",
						"name": "Role",
						"type": "uint8"
					}
				],
				"internalType": "struct name.User",
				"name": "",
				"type": "tuple"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]