import Cards
        
def main():
    
    print('Welcome to war!')
    
    while(True):
        
        user_input = input('Would you like to start the game? [y/n]')
                
        if user_input.lower() in ['yes', 'y', 'ya']:
            print('Start game')
        elif user_input.lower() in ['no', 'n', 'nah']:
            print('Quitting game')
            break
        else:
            print('Invalid input')
            
if __name__ == '__main__':
    main()