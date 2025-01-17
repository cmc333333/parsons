petition_test_data = {
    'petitions': [{
        'admin_events_status': 'auto',
        'admin_status': 'unreviewed',
        'alias': None,
        'campaigner_contactable': True,
        'can_download_signers': True,
        'created_at': '2021-11-17T22:51:56Z',
        'custom_goal': None,
        'delivery_details': None,
        'external_facebook_page': None,
        'external_site': None, 'goal': 100,
        'hide_petition_creator': None,
        'hide_recent_signers': None,
        'hide_signature_form': None, 'id': 536084,
        'launched': True, 'locale': 'en',
        'petition_creator_name_override': None,
        'redirect_to': None, 'show_progress_bar': True,
        'signature_count_add_amount': None,
        'slug': 'test-1475', 'source': None, 'title': 'Test',
        'updated_at': '2021-11-17T22:51:58Z', 'what': 'Test Petition', 'who': 'Test Rep',
        'why': 'This is a test.',
        'title_locked': None,
        'who_locked': None, 'what_locked': None, 'why_locked': None,
        'delivery_details_locked': None,
        'external_facebook_page_locked': None,
        'external_site_locked': None,
        'categories_locked': None,
        'url': 'http://test.controlshift.app/petitions/test-1475',
        'public_who': 'Test Rep',
        'ended': False, 'successful': False,
        'image': None, 'public_signature_count': 1,
        'admin_notes': [],
        'creator': {
            'full_name': 'foo', 'first_name': 'foo', 'last_name':
            'bar', 'email': 'foo@bar.org',
            'phone_number': None},
        'mentor': None,
        'reviewer': None, 'location': None,
        'decision_makers': [], 'effort': None,
        'partnership': None, 'labels': [],
        'categories': []
    }],
    "meta": {
        "current_page": 1,
        "total_pages": 1,
        "previous_page": None,
        "next_page": None
    }
}

expected_petition_columns = [
    'admin_events_status', 'admin_status', 'alias', 'campaigner_contactable',
    'can_download_signers', 'created_at', 'custom_goal', 'delivery_details',
    'external_facebook_page', 'external_site', 'goal', 'hide_petition_creator',
    'hide_recent_signers', 'hide_signature_form', 'id', 'launched', 'locale',
    'petition_creator_name_override', 'redirect_to', 'show_progress_bar',
    'signature_count_add_amount', 'slug',
    'source', 'title', 'updated_at', 'what', 'who', 'why', 'title_locked', 'who_locked',
    'what_locked', 'why_locked', 'delivery_details_locked', 'external_facebook_page_locked',
    'external_site_locked', 'categories_locked', 'url', 'public_who', 'ended', 'successful',
    'image', 'public_signature_count', 'admin_notes', 'creator', 'mentor', 'reviewer',
    'location', 'decision_makers', 'effort', 'partnership', 'labels', 'categories']
