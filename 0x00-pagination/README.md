This project focuses on implementing pagination functionalities in Python, particularly for a dataset of popular baby names. The dataset is provided in a CSV file named Popular_Baby_Names.csv. The project covers three main tasks: Simple helper function, Simple pagination, Hypermedia pagination, and Deletion-resilient hypermedia pagination.

Resources
REST API Design: Pagination
HATEOAS
Learning Objectives
Understand how to paginate a dataset with simple page and page_size parameters.
Implement pagination with hypermedia metadata.
Design deletion-resilient pagination methods.
Tasks
0. Simple helper function
File: 0-simple_helper_function.py

Implement a function index_range that returns a tuple containing start and end indexes for pagination based on page and page_size parameters.
1. Simple pagination
File: 1-simple_pagination.py

Implement a Server class with methods to paginate a dataset of popular baby names.
Implement get_page method to return a paginated dataset based on page and page_size.
Validate input parameters using assert statements.
2. Hypermedia pagination
File: 2-hypermedia_pagination.py

Replicate index_range and Server class from previous tasks.
Implement get_hyper method to return paginated data with hypermedia metadata.
Hypermedia metadata should include page_size, page, data, next_page, prev_page, and total_pages.
3. Deletion-resilient hypermedia pagination
File: 3-hypermedia_del_pagination.py

Extend Server class with methods to handle deletion-resilient pagination.
Implement get_hyper_index method to return paginated data considering possible deletions between queries.
Ensure the method is resilient to deletions, maintaining pagination consistency.
