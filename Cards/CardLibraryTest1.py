import Cards

def main():
    d = Cards.Deck()
    print ('Initial deck value')
    print (d)
    d.shuffle()
    print('Shuffled deck value')
    print(d)
    
    player1 = Cards.Hand()
    d.deal_card(player1)
    print('Dealing a card to player 1')
    print(player1)
    
    d.deal_card(player1)
    print('Dealing another card to player 1')
    print(player1)
    
if __name__ == '__main__':
    main()
    