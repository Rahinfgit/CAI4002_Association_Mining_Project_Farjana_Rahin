
### Interactive Supermarket Simulation with Association Rule Mining

#### Author Information

- **Name**: Farjana Rahin
- **Student ID**: 6517691
- **Course**: CAI 4002 - Artificial Intelligence
- **Semester**: Fall 2025

#### System Overview
This application loads supermarket transactional data, preprocesses it, and runs Apriori and Eclat association rule mining algorithms. It then provides an interactive console-based product recommendation system showing confidence values and qualitative strength ratings.

#### Technical Stack
- Python 3.x
- Standard libraries: csv, itertools, collections, time

#### Installation & Usage
1. Place products.csv and sample_transactions.csv in the data folder.
2. Run: `python src/main.py`
3. Enter support/confidence thresholds or press Enter for defaults.
4. Use the interactive query engine to test recommendations.

#### Algorithms Implemented
- Apriori: level-wise candidate generation, Apriori property pruning.
- Eclat: vertical TID-set intersections, depth-first search.
- Rule Generation: support & confidence thresholds, sorted by confidence.

#### Preprocessing & Cleaning Summary
- Standardizes item case.
- Removes duplicates.
- Filters invalid product names.
- Removes empty and single-item transactions.

#### Performance Summary
Apriori and Eclat were benchmarked using default thresholds (min_support=0.2, min_confidence=0.5). Eclat performed faster due to TID-set intersections.

#### Testing
Includes cleaning tests, duplicate-handling tests, and recommendation tests.

#### Limitations
Console UI only, assumes dataset fits in memory, CLOSET not implemented.

#### AI Tool Usage
ChatGPT assisted in producing documentation and structuring the project. All code was reviewed and understood by the student.

#### References
- Course lecture notes
- Standard Apriori/Eclat literature
- Python documentation
