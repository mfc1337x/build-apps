class Config:
    REVANCED_APKS_RELEASE_URL = (
        "https://api.github.com/repos/mfc1337x/build-apps/releases/latest"
    )
    MICROG_RELEASE_URL = (
        "https://github.com/ReVanced/GmsCore/releases/latest"
    )
    REVANCED_CHANGES_URL = (
        "https://api.github.com/repos/revanced/revanced-patches/compare"
    )
    REVANCED_EXTENDED_CHANGES_URL = (
        "https://api.github.com/repos/inotia00/revanced-patches/compare"
    )
    
    CREDITS_MESSAGE = "1337x"

    RELEASE_MESSAGE = """📑 *RELEASE* {release_name}

[Release notes and changelogs (What's New)]({changelogs_url})

📦 *Downloads* 

{nonroot_files}

{credits_message}
    
@ReVancedStableReleases | 1337x"""
