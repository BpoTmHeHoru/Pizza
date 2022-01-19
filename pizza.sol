//SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.10;
pragma abicoder v2;

contract name {

    uint Totaladmin = 0;


   enum Roles {
       user, admin, manager
   }
   
    // [+] Structures
    struct User {
        string[3] Fio;
        string login;
        string pass;
        Roles Role;
    }

    struct Item {
        string Name;
        string Description;
        string Ingridients;
        uint Price;
        uint ItemId;
    }

    struct Basket {
        string Name;
        uint FulPrice;
        uint Id;

    }

    //[+] Маппинг
    mapping (address => User) Users;
    mapping (address => bool) RegisteredUser;
    mapping (address => Basket) UserBasket;

      // [+] Arrays 
    Item[] Itemes;  // <= [+] drink is added here
    Basket[] Items;  // <= [+] Items 

    constructor() {
        
        Users[msg.sender].Role = Roles.admin; // смена роли
        Totaladmin = 1;

        Itemes.push(Item("Pepperoni", "Ochen vikusnii pizza", "Myaso C# WSRchikov", 499, 1)); 
        Itemes.push(Item("Ostrov otchayaniya", "Ochen vikusnii pizza", "Bol i stradaniya blockchainerov", 999, 2));
        Itemes.push(Item("4 Porcii boli", "Ochen vikusnii pizza", "10 ne vispavchihsya studentov iz 10", 699, 3));

        Itemes.push(Item("Baltika 0", "Ochen vikusnii Baltika", "Slezi Blockchainerov", 199, 4));
        Itemes.push(Item("Otec Gusya", "Ne pei eto", "10 ne vispavchihsya blockchainerov iz 10", 99, 5));
        Itemes.push(Item("Baltika 1234", "Ochen vikusnii Baltika", "Y menya net slov", 49, 6));
    }

    modifier YouIsRegistered {
        require(RegisteredUser[msg.sender] == true, "You are not registered"); 
        _; 
    }

    
    modifier ThatUserIsRegistered(address _who)
    {
        require(RegisteredUser[_who] == true); // Проверяем любого пользователя, зареган ли он
        _;
    }

    modifier IsAdmin
    {
        require(Users[msg.sender].Role == Roles.admin); //Проверяем роль текущего пользователя - она должна быть Админ
        _;
    }

    modifier IsManager
    {
        require(Users[msg.sender].Role == Roles.manager); //Проверяем роль текущего пользователя - она должна быть Менеджер
        _;
    }

    modifier IsUser
    {
        require(Users[msg.sender].Role == Roles.user); //Проверяем роль текущего пользователя - она должна быть Юзер
        _;
    }

    function Registr(string[3] memory Fio, string memory login, string memory pass) public {
        require(RegisteredUser[msg.sender] == false); // [-] Ты не зарегистрирован!ф
        require(bytes(login).length >= 3 && bytes(login).length <= 10);
        require(bytes(pass).length >= 3 && bytes(pass).length <= 10);
        Users[msg.sender] = User(Fio, login, pass, Roles.user);
        RegisteredUser[msg.sender] = true; // [+] Ты зарегистрирован!
    }

    function Auth(string memory login, string memory pass) public view returns (User memory) {   
        require (keccak256(bytes(login))==keccak256(bytes(Users[msg.sender].login)));
        require (keccak256(bytes(pass))==keccak256(bytes(Users[msg.sender].pass)));
        return Users[msg.sender];
    }

    
    function ChangeAdminToManagerOrUser(string memory _Role) public IsAdmin
    {
        if(Totaladmin == 1)
            revert("You last Admin, you can't change role"); //Выкидываем исключение, и пишем инфу о нём

        if(keccak256(bytes(_Role)) == keccak256(bytes("Manager")) || keccak256(bytes(_Role)) == keccak256(bytes("manager")))
        {
            Users[msg.sender].Role = Roles.manager; 
            Totaladmin--; //Уменьшаем количество админов на 1
        }

        else if(keccak256(bytes(_Role)) == keccak256(bytes("User")) || keccak256(bytes(_Role)) == keccak256(bytes("user")))
        {
            Users[msg.sender].Role = Roles.user; //Ставим роль Юзера
            Totaladmin--;
        }
    }

    //Добавляем нового админа в систему
    function AddNewAdmin(address _toaddr) public IsAdmin { 
        Users[_toaddr].Role = Roles.admin;
        Totaladmin++;
    }

    //Добавляем нового менеджера
    function AddNewManager(address _toaddr) public IsAdmin {
        Users[_toaddr].Role = Roles.manager;
    }
//<End Функционал для админа>

//<Функционал менеджера>
    
    function AddNewItem1(string memory Name, string memory Description, string memory Ingridients, uint Price, uint ItemId)
    public IsManager {
        Itemes.push(Item(Name, Description, Ingridients, Price, ItemId));
    }

    //Смена роли до юзера
    function ChangeManagerToUser() public IsManager {
        Users[msg.sender].Role = Roles.user;
    }
//<End Функционал менеджера>

//<Функционал юзера>
   function AddBasket(string memory Name, uint FulPrice, uint Id) public IsUser {
        Items.push(Basket(Name, FulPrice, Id));
    } 
    
    function FullPrice(uint FulPrice) public view returns(uint) {
        uint FPrice;
        for(uint i=0; i < Items.length; i++) {
        FPrice += Items[i].FulPrice;
        }
        return FPrice;
    }   


    function ReturnBasket() public view returns(Basket[] memory) {
        return Items;
    }
   
//<End Функционал юзера>

//<Общий функционал>
    //Посмотреть информацию о текущем пользователе
    function ViewLk() public view returns(User memory) {
        return Users[msg.sender];
    }
    
    function ViewAllItems() public view returns(Item[] memory) {
        return Itemes;
    } 

}




