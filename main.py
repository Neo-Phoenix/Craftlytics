import argparse

def main():
    parser = argparse.ArgumentParser(
                    prog='craftlytics',
                    description='Craftlytics - Analyze Minecraft crafting recipes.')
    
    # arguments
    parser.add_argument('-a', '--analyze', action='store_true', help="Run the analysis on all recipes")

    args = parser.parse_args()
    if args.analyze:
        # parser.py load in jsons from 'all_crafting_recipes_24w46a'

        # tracker.py
        # decodes to a dictionary containing type/categories, 
        # which contains total_counts, occurrences and a recipes list of ids 

        # exporter.py
        # export to a list.txt or other format based on args
        print("Hello, World!")
        

if __name__ == "__main__":
    main()