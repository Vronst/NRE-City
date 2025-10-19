"""Script for processig city data."""

import data_processor as p


def main():
    """Placeholder."""
    loader = p.DataLoader("data.json")
    processor = p.CityProcessor(loader)

    print(processor.process_changes())


if __name__ == "__main__":
    main()
