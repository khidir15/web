DJ_PIPELINE = {
    'COMPILERS': ('app.compilers.ES6Compiler', ),
    'CSS_COMPRESSOR': 'pipeline.compressors.yuglify.YuglifyCompressor',
    'JS_COMPRESSOR': 'pipeline.compressors.uglifyjs.UglifyJSCompressor',
    'BABEL_BINARY': 'npx babel',
    'STYLESHEETS': {
        'ens': {
            'source_filenames': (
                'v2/css/bootstrap.min.css',
                'v2/css/lib/typography.css',
                'v2/css/gitcoin.css',
                'onepager/css/main.css',
                'v2/css/box_redeem.css',
                'v2/css/rain.css',
                'v2/css/forms/button.css',
                'v2/css/external_bounties/checkboxes.css',
                'v2/css/jquery.select2.min.css',
                'cookielaw/css/cookielaw.css',
            ),
            'output_filename': 'bundle/css/ens.min.css',
        },
        'head': {
            'source_filenames': (
                'v2/css/fontawesome-all.min.css',
                'v2/css/bootstrap.min.css',
                'v2/css/lib/typography.css',
                'v2/css/gitcoin.css',
                'v2/css/base.css',
                'v2/css/jquery-ui.css',
                'v2/css/jquery.modal.min.css',
                'v2/css/jquery.select2.min.css',
                'v2/css/animate.min.css',
                'v2/css/rain.css',
                'v2/css/buttons.css',
                'v2/css/timeline.css',
                'v2/css/carousel.css',
                'v2/css/faucet.css',
                'v2/css/colors.css',
                'v2/css/typography.css',
                # Forms
                'v2/css/forms/button.css',
                'v2/css/forms/checkbox.css',
                'v2/css/forms/form.css',
                'v2/css/forms/input.css',
                'v2/css/forms/label.css',
                'v2/css/forms/radio.css',
                'v2/css/forms/select.css',
                'v2/css/external_bounties/checkboxes.css',
                'cookielaw/css/cookielaw.css',
            ),
            'output_filename': 'bundle/css/head.min.css',
        },
        'ios': {
            'source_filenames': (
                'v2/css/toolbox.css',
                'v2/css/card.css',
                'v2/css/ios.css',
            ),
            'output_filename': 'bundle/css/ios.min.css',
        }
    },
    'JAVASCRIPT': {
        'external_bounties': {
            'source_filenames': (
                'v2/js/tokens.js',
                'v2/js/pages/offchain_bounties.js',
                'v2/js/shared.js',
            ),
            'output_filename': 'bundle/js/externalbounties.min.js',
        },
        'faucet': {
            'source_filenames': (
                'v2/js/amounts.js',
                'v2/js/abi.js',
                'v2/js/tokens.js',
                'v2/js/pages/faucet_form.js',
                'v2/js/pages/process_faucet.js',
                'v2/js/shared.js',
            ),
            'output_filename': 'bundle/js/faucet.min.js',
        },
        'footer_full': {
            'source_filenames': (
                'v2/js/jquery.js',
                'v2/js/jquery.cookie.js',
                'v2/js/jquery-ui.js',
                'v2/js/tooltip.js',
                'v2/js/jquery.modal.min.js',
                'v2/js/jquery.select2.min.js',
                'v2/js/jquery.validate.min.js',
                'v2/js/jsrender.js',
                'v2/js/base.js',
                'v2/js/purify.min.js',
                'v2/js/shared.js',
                'v2/js/work_with_gitcoin.js',
                'v2/js/animate.min.js',
                'v2/js/note.js',
                'v2/js/pages/carousel.js',
                'cookielaw/js/cl.js',
            ),
            'output_filename': 'bundle/js/footer.min.js',
        },
        'footer_slim': {
            'source_filenames': (
                'v2/js/jquery.js',
                'v2/js/jquery.cookie.js',
                'v2/js/jquery.modal.min.js',
                'v2/js/jquery.select2.min.js',
                'v2/js/jquery.validate.min.js',
                'v2/js/jsrender.js',
                'v2/js/base.js',
                'v2/js/purify.min.js',
                'v2/js/shared.js',
                'v2/js/work_with_gitcoin.js',
                'v2/js/animate.min.js',
                'v2/js/note.js',
                'v2/js/pages/carousel.js',
                'cookielaw/js/cl.js',
            ),
            'output_filename': 'bundle/js/slim_footer.min.js',
        },
    }
}
