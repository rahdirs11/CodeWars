class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.itemsPerPage = items_per_page

    def item_count(self):
        return len(self.collection)

    def page_count(self):
        from math import ceil
        return ceil(self.item_count() / self.itemsPerPage)

    def page_item_count(self, page_index):
        totalPageCount = self.page_count()
        if page_index >= totalPageCount:
            return -1
        result, itemCount = self.itemsPerPage, self.item_count()
        if itemCount % result != 0 and page_index == totalPageCount - 1:
            result = itemCount % self.itemsPerPage
        return result

    def page_index(self, item_index):
        if not item_index in range(1, self.item_count() + 1):
            return -1
        from math import ceil
        return ceil(item_index / self.itemsPerPage) - 1
