class Person(object):

    def __init__(self, identifier, identifier_image, results, result_image, confirmed_identifier, confirmed_results):
        self._identifier = identifier
        self._identifier_image = identifier_image
        self._results = results
        self._result_image = result_image
        if confirmed_identifier == "":
            confirmed_identifier = identifier
        self._confirmed_identifier = confirmed_identifier
        if len(confirmed_results) == 0:
            confirmed_results = results
        self._confirmed_results = confirmed_results

    def dump(self):
        return {
            'identifier': self._identifier,
            'identifier_image': self._identifier_image,
            'results': self._results,
            'result_image': self._result_image,
            'confirmed_identifier': self._confirmed_identifier,
            'confirmed_results': self._confirmed_results
        }

    def get_id(self):
        return self._identifier

    def set_id(self, new_id):
        self._identifier = new_id

    def get_id_image(self):
        return self._identifier_image

    def set_id_image(self, new_id_img):
        self._identifier_image = new_id_img

    def get_results(self):
        return self._results

    def set_results(self, new_results):
        self._results = new_results

    def get_result_image(self):
        return self._result_image

    def set_result_image(self, new_res_image):
        self._result_image = new_res_image

    def get_confirmed_id(self):
        return self._confirmed_identifier

    def set_confirmed_id(self, new_cnfmd_id):
        self._confirmed_identifier = new_cnfmd_id

    def get_confirmed_results(self):
        return self._confirmed_results

    def set_confirmed_results(self, new_cnfmd_res):
        self._confirmed_results = new_cnfmd_res
