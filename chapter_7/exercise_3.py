if __name__ == "__main__":
    cin = ''
    summer = 0
    while cin != 'end':
        try:
            cin = input('Enter an integer: ')
            float(cin)
            summer = summer + float(cin)
        except ValueError:
            print('non - numeric value entered')
        except KeyboardInterrupt:
            print('you cant escape!')
        except EOFError:
            print(summer)
            break
        except:
            print('an error has occured')
