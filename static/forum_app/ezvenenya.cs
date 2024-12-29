bool ezvenenya = false;

if (!ezvenenya) {
    Console.WriteLine("чорт беги отсюда чорт дон");
    preora preora = new preora();
    preora.brat1 = "братПовере1";
    preora.brat2 = "братПовере2";
    preora.brat3 = "братПовере3";
    preora.brat4 = "братПовере4";
    preora.brat5 = "братПовере5";

    string[] brats = { preora.brat1, preora.brat2, preora.brat3, preora.brat4, preora.brat5 };
    for (int i = 0; i < brats.Length; i++) {
        Console.WriteLine("БратьяПовере: " + brats[i]);
    }
} else {
    Console.WriteLine("42 братух");
}


class preora {
    public string brat1;
    public string brat2;
    public string brat3;
    public string brat4;
    public string brat5;
}