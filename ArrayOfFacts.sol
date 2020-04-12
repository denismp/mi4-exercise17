pragma solidity ^0.6.1;

contract ArrayOfFacts {
    string[] private facts;
    address private contractOwner;

    constructor() public {
        contractOwner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == contractOwner, "You must be the Contract owner");
        _;
    }

    function add(string memory newFact) public onlyOwner {
        facts.push(newFact);
    }

    function count() public view returns (uint256) {
       return facts.length;
    }

    function getFact(uint256 index) public view returns (string memory) {
        return facts[index];
    }
}