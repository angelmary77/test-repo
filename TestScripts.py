ATHYAM_THEATRE_ALL_SCREENS =\
    {
        "id": "492765b5-5698-4b89-8ad7-fccad32b9d6b",
        "screens":
            [
                {"id": "6257f846-7f25-4dd8-853e-acdc98049864",
                "devices": ["48c7b38e-c1e8-40ef-9d25-40c6174ab96a",
                            "a23f12d2-0b0e-49ee-9392-25bcdcbd1d99"]},
                {"id": "05e9a828-1b8c-456c-b651-4dc69985d172",
                 "devices": ["a01d2cfa-d214-4816-9bdf-139ead2562c0",
                             "f7e8b7e7-808d-4f76-9ad1-4e27a5b4384f"]},
                {"id": "07a8ebfe-db66-42bb-9382-97cfabe2f9dc",
                               "devices": ["1120f13e-3842-43a2-87bb-64e6baded497"]}
            ]
    }

SATHYAM_THEATRE_PARTIAL_SCREENS = {
        "id": "492765b5-5698-4b89-8ad7-fccad32b9d6b",
        "screens":[
                        {"id": "6257f846-7f25-4dd8-853e-acdc98049864",
                         "devices": ["48c7b38e-c1e8-40ef-9d25-40c6174ab96a",
                                     "a23f12d2-0b0e-49ee-9392-25bcdcbd1d99"]},
                        {"id": "05e9a828-1b8c-456c-b651-4dc69985d172",
                         "devices": ["a01d2cfa-d214-4816-9bdf-139ead2562c0",
                                     "f7e8b7e7-808d-4f76-9ad1-4e27a5b4384f"]}
                           ]
                         }

ESCAPE_THEATRE_PARTIAL_SCREENS = {"id": "f7e5f00d-6b17-4602-bdde-4a1ec782a7a2",
                                 "screens":
                                [
                                   {"id": "7e702022-592c-4d78-90f6-e8ea60fb2560",
                                     "devices": ["1f598bc8-38c4-43ba-8f69-4882fd1a5c07",
                                                          "9f984124-ad7a-4f1a-b7f2-1aa7d38c22f4"]}
                                 ]
                               }

COMPOSITION_ID_1 = "ee2bc9ed-de0a-4942-b517-38eb86da5495"
COMPOSITION_ID_2 = "88866354-56c5-48b3-a357-3cc7b9c0bc01"

kdmRequest = {
       'bookingNo': "",
       "creationTime": "12:30AM",
       "kdms": []
   }

kdms = {
       "compositionId": "UUID",
       "facilityId": "Theatre UUID. Required",
       "auditoriumId": "Screen UUID. Optional. Empty if booking is for whole theatre",
       }