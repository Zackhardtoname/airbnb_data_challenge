# from sklearn.svm import SVR
# from sklearn.feature_selection import RFE
# from sklearn.feature_selection import SelectKBest
# from sklearn.feature_selection import chi2
# # g = df.columns.to_series().groupby(df.dtypes).groups
# for s in ['name', 'summary', 'space',
#         'description', 'experiences_offered', 'neighborhood_overview', 'notes',
#         'transit', 'access', 'interaction', 'house_rules', 'picture_url',
#         'host_url', 'host_name', 'host_since', 'host_location', 'host_about',
#         'host_response_time', 'host_response_rate', 'host_is_superhost',
#         'host_thumbnail_url', 'host_picture_url', 'host_neighbourhood',
#         'host_verifications', 'host_has_profile_pic', 'host_identity_verified',
#         'street', 'neighbourhood', 'neighbourhood_cleansed', 'city', 'state',
#         'zipcode', 'market', 'smart_location', 'country_code', 'country',
#         'is_location_exact', 'property_type', 'room_type', 'bed_type',
#         'amenities', 'weekly_price', 'monthly_price', 'security_deposit',
#         'cleaning_fee', 'extra_people', 'calendar_updated', 'has_availability',
#         'calendar_last_scraped', 'first_review', 'last_review',
#         'requires_license', 'license', 'jurisdiction_names', 'instant_bookable',
#         'is_business_travel_ready', 'cancellation_policy',
#         'require_guest_profile_picture', 'require_guest_phone_verification']:
#     print(s)
#     print(df[s].head())
#     print(df[s].describe())
#     print("-------------------------")
#
# # check if two cols are the same
# arr = "diff" in np.where(df['runs1']==df['runs2'], 'same', 'diff')
# np.unique(arr, return_counts=True)
#
# # Feature Elimination
#
# %% q
#
# estimator = SVR(kernel="linear")
# selector = RFE(estimator, 5, step=1)
# selector = selector.fit(X, y)
# selector.support_
#
#
# %%
#
# selector.ranking_
# for i in range(len(list(X))):
#     if selector.ranking_[i] == 1:
#         print(list(X)[i])
#
# # for col in cat_attribs:
# #     print(df[col].value_counts())
# sparse.save_npz("../data/X.npz", X)
#
# primary_num_cols = [
#       "minimum_nights", "maximum_nights",
#      "square_feet",
#      #"calendar_updated" is a bit tricky; handle it later
# ]
#
# are all of the "primary_num_cols" in data keys, "instant_bookable", "host_has_profile_pic", "host_identity_verified",
# "description", "neighborhood_overview", "transit", "house_rules",
# pictures of the listings as well as host profile pictures, and in fact, the past availability (although we could not use this one since we mostly only have aggregated availability statistics).
#
# dark horses:
# room_type
#
# transformed:
# log_bedrooms_per_accommodates
#
# less:
# response_time
# property_type
