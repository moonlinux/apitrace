##########################################################################
#
# Copyright 2013 VMware, Inc.
# Copyright 2011 LunarG, Inc.
# All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
##########################################################################/


"""EGL enum description"""


from .stdapi import *

# Most of the following content was produced in a semi-automated fashion by
# the scripts/eglenum.sed sed script.
EGLenum = Enum("EGLenum", [
    "EGL_DISPLAY_SCALING",		# 0x2710
    "EGL_SUCCESS",		# 0x3000
    "EGL_NOT_INITIALIZED",		# 0x3001
    "EGL_BAD_ACCESS",		# 0x3002
    "EGL_BAD_ALLOC",		# 0x3003
    "EGL_BAD_ATTRIBUTE",		# 0x3004
    "EGL_BAD_CONFIG",		# 0x3005
    "EGL_BAD_CONTEXT",		# 0x3006
    "EGL_BAD_CURRENT_SURFACE",		# 0x3007
    "EGL_BAD_DISPLAY",		# 0x3008
    "EGL_BAD_MATCH",		# 0x3009
    "EGL_BAD_NATIVE_PIXMAP",		# 0x300A
    "EGL_BAD_NATIVE_WINDOW",		# 0x300B
    "EGL_BAD_PARAMETER",		# 0x300C
    "EGL_BAD_SURFACE",		# 0x300D
    "EGL_CONTEXT_LOST",		# 0x300E
    "EGL_BUFFER_SIZE",		# 0x3020
    "EGL_ALPHA_SIZE",		# 0x3021
    "EGL_BLUE_SIZE",		# 0x3022
    "EGL_GREEN_SIZE",		# 0x3023
    "EGL_RED_SIZE",		# 0x3024
    "EGL_DEPTH_SIZE",		# 0x3025
    "EGL_STENCIL_SIZE",		# 0x3026
    "EGL_CONFIG_CAVEAT",		# 0x3027
    "EGL_CONFIG_ID",		# 0x3028
    "EGL_LEVEL",		# 0x3029
    "EGL_MAX_PBUFFER_HEIGHT",		# 0x302A
    "EGL_MAX_PBUFFER_PIXELS",		# 0x302B
    "EGL_MAX_PBUFFER_WIDTH",		# 0x302C
    "EGL_NATIVE_RENDERABLE",		# 0x302D
    "EGL_NATIVE_VISUAL_ID",		# 0x302E
    "EGL_NATIVE_VISUAL_TYPE",		# 0x302F
    "EGL_SAMPLES",		# 0x3031
    "EGL_SAMPLE_BUFFERS",		# 0x3032
    "EGL_SURFACE_TYPE",		# 0x3033
    "EGL_TRANSPARENT_TYPE",		# 0x3034
    "EGL_TRANSPARENT_BLUE_VALUE",		# 0x3035
    "EGL_TRANSPARENT_GREEN_VALUE",		# 0x3036
    "EGL_TRANSPARENT_RED_VALUE",		# 0x3037
    "EGL_NONE",		# 0x3038
    "EGL_BIND_TO_TEXTURE_RGB",		# 0x3039
    "EGL_BIND_TO_TEXTURE_RGBA",		# 0x303A
    "EGL_MIN_SWAP_INTERVAL",		# 0x303B
    "EGL_MAX_SWAP_INTERVAL",		# 0x303C
    "EGL_LUMINANCE_SIZE",		# 0x303D
    "EGL_ALPHA_MASK_SIZE",		# 0x303E
    "EGL_COLOR_BUFFER_TYPE",		# 0x303F
    "EGL_RENDERABLE_TYPE",		# 0x3040
    "EGL_MATCH_NATIVE_PIXMAP",		# 0x3041
    "EGL_CONFORMANT",		# 0x3042
    "EGL_MATCH_FORMAT_KHR",		# 0x3043
    "EGL_SLOW_CONFIG",		# 0x3050
    "EGL_NON_CONFORMANT_CONFIG",		# 0x3051
    "EGL_TRANSPARENT_RGB",		# 0x3052
    "EGL_VENDOR",		# 0x3053
    "EGL_VERSION",		# 0x3054
    "EGL_EXTENSIONS",		# 0x3055
    "EGL_HEIGHT",		# 0x3056
    "EGL_WIDTH",		# 0x3057
    "EGL_LARGEST_PBUFFER",		# 0x3058
    "EGL_DRAW",		# 0x3059
    "EGL_READ",		# 0x305A
    "EGL_CORE_NATIVE_ENGINE",		# 0x305B
    "EGL_NO_TEXTURE",		# 0x305C
    "EGL_TEXTURE_RGB",		# 0x305D
    "EGL_TEXTURE_RGBA",		# 0x305E
    "EGL_TEXTURE_2D",		# 0x305F
    "EGL_Y_INVERTED_NOK",		# 0x307F
    "EGL_TEXTURE_FORMAT",		# 0x3080
    "EGL_TEXTURE_TARGET",		# 0x3081
    "EGL_MIPMAP_TEXTURE",		# 0x3082
    "EGL_MIPMAP_LEVEL",		# 0x3083
    "EGL_BACK_BUFFER",		# 0x3084
    "EGL_SINGLE_BUFFER",		# 0x3085
    "EGL_RENDER_BUFFER",		# 0x3086
    "EGL_COLORSPACE",		# 0x3087
    "EGL_ALPHA_FORMAT",		# 0x3088
    "EGL_COLORSPACE_sRGB",		# 0x3089
    "EGL_COLORSPACE_LINEAR",		# 0x308A
    "EGL_ALPHA_FORMAT_NONPRE",		# 0x308B
    "EGL_ALPHA_FORMAT_PRE",		# 0x308C
    "EGL_CLIENT_APIS",		# 0x308D
    "EGL_RGB_BUFFER",		# 0x308E
    "EGL_LUMINANCE_BUFFER",		# 0x308F
    "EGL_HORIZONTAL_RESOLUTION",		# 0x3090
    "EGL_VERTICAL_RESOLUTION",		# 0x3091
    "EGL_PIXEL_ASPECT_RATIO",		# 0x3092
    "EGL_SWAP_BEHAVIOR",		# 0x3093
    "EGL_BUFFER_PRESERVED",		# 0x3094
    "EGL_BUFFER_DESTROYED",		# 0x3095
    "EGL_OPENVG_IMAGE",		# 0x3096
    "EGL_CONTEXT_CLIENT_TYPE",		# 0x3097
    "EGL_CONTEXT_MAJOR_VERSION",		# 0x3098
    "EGL_MULTISAMPLE_RESOLVE",		# 0x3099
    "EGL_MULTISAMPLE_RESOLVE_DEFAULT",		# 0x309A
    "EGL_MULTISAMPLE_RESOLVE_BOX",		# 0x309B
    "EGL_CL_EVENT_HANDLE",		# 0x309C
    "EGL_GL_COLORSPACE",		# 0x309D
    "EGL_OPENGL_ES_API",		# 0x30A0
    "EGL_OPENVG_API",		# 0x30A1
    "EGL_OPENGL_API",		# 0x30A2
    "EGL_NATIVE_PIXMAP_KHR",		# 0x30B0
    "EGL_GL_TEXTURE_2D",		# 0x30B1
    "EGL_GL_TEXTURE_3D",		# 0x30B2
    "EGL_GL_TEXTURE_CUBE_MAP_POSITIVE_X",		# 0x30B3
    "EGL_GL_TEXTURE_CUBE_MAP_NEGATIVE_X",		# 0x30B4
    "EGL_GL_TEXTURE_CUBE_MAP_POSITIVE_Y",		# 0x30B5
    "EGL_GL_TEXTURE_CUBE_MAP_NEGATIVE_Y",		# 0x30B6
    "EGL_GL_TEXTURE_CUBE_MAP_POSITIVE_Z",		# 0x30B7
    "EGL_GL_TEXTURE_CUBE_MAP_NEGATIVE_Z",		# 0x30B8
    "EGL_GL_RENDERBUFFER",		# 0x30B9
    "EGL_VG_PARENT_IMAGE_KHR",		# 0x30BA
    "EGL_GL_TEXTURE_LEVEL",		# 0x30BC
    "EGL_GL_TEXTURE_ZOFFSET",		# 0x30BD
    "EGL_POST_SUB_BUFFER_SUPPORTED_NV",		# 0x30BE
    "EGL_CONTEXT_OPENGL_ROBUST_ACCESS_EXT",		# 0x30BF
    "EGL_FORMAT_RGB_565_EXACT_KHR",		# 0x30C0
    "EGL_FORMAT_RGB_565_KHR",		# 0x30C1
    "EGL_FORMAT_RGBA_8888_EXACT_KHR",		# 0x30C2
    "EGL_FORMAT_RGBA_8888_KHR",		# 0x30C3
    "EGL_MAP_PRESERVE_PIXELS_KHR",		# 0x30C4
    "EGL_LOCK_USAGE_HINT_KHR",		# 0x30C5
    "EGL_BITMAP_POINTER_KHR",		# 0x30C6
    "EGL_BITMAP_PITCH_KHR",		# 0x30C7
    "EGL_BITMAP_ORIGIN_KHR",		# 0x30C8
    "EGL_BITMAP_PIXEL_RED_OFFSET_KHR",		# 0x30C9
    "EGL_BITMAP_PIXEL_GREEN_OFFSET_KHR",		# 0x30CA
    "EGL_BITMAP_PIXEL_BLUE_OFFSET_KHR",		# 0x30CB
    "EGL_BITMAP_PIXEL_ALPHA_OFFSET_KHR",		# 0x30CC
    "EGL_BITMAP_PIXEL_LUMINANCE_OFFSET_KHR",		# 0x30CD
    "EGL_LOWER_LEFT_KHR",		# 0x30CE
    "EGL_UPPER_LEFT_KHR",		# 0x30CF
    "EGL_IMAGE_PRESERVED",		# 0x30D2
    #"EGL_SHARED_IMAGE_NOK",		# 0x30DA
    "EGL_COVERAGE_BUFFERS_NV",		# 0x30E0
    "EGL_COVERAGE_SAMPLES_NV",		# 0x30E1
    "EGL_DEPTH_ENCODING_NV",		# 0x30E2
    "EGL_DEPTH_ENCODING_NONLINEAR_NV",		# 0x30E3
    "EGL_SYNC_PRIOR_COMMANDS_COMPLETE_NV",		# 0x30E6
    "EGL_SYNC_STATUS_NV",		# 0x30E7
    "EGL_SIGNALED_NV",		# 0x30E8
    "EGL_UNSIGNALED_NV",		# 0x30E9
    "EGL_ALREADY_SIGNALED_NV",		# 0x30EA
    "EGL_TIMEOUT_EXPIRED_NV",		# 0x30EB
    "EGL_CONDITION_SATISFIED_NV",		# 0x30EC
    "EGL_SYNC_TYPE_NV",		# 0x30ED
    "EGL_SYNC_CONDITION_NV",		# 0x30EE
    "EGL_SYNC_FENCE_NV",		# 0x30EF
    "EGL_SYNC_PRIOR_COMMANDS_COMPLETE",		# 0x30F0
    "EGL_SYNC_STATUS",		# 0x30F1
    "EGL_SIGNALED",		# 0x30F2
    "EGL_UNSIGNALED",		# 0x30F3
    "EGL_TIMEOUT_EXPIRED",		# 0x30F5
    "EGL_CONDITION_SATISFIED",		# 0x30F6
    "EGL_SYNC_TYPE",		# 0x30F7
    "EGL_SYNC_CONDITION",		# 0x30F8
    "EGL_SYNC_FENCE",		# 0x30F9
    "EGL_SYNC_REUSABLE_KHR",		# 0x30FA
    "EGL_CONTEXT_MINOR_VERSION",		# 0x30FB
    "EGL_CONTEXT_FLAGS_KHR",		# 0x30FC
    "EGL_CONTEXT_OPENGL_PROFILE_MASK",		# 0x30FD
    "EGL_SYNC_CL_EVENT",		# 0x30FE
    "EGL_SYNC_CL_EVENT_COMPLETE",		# 0x30FF
    "EGL_CONTEXT_PRIORITY_LEVEL_IMG",		# 0x3100
    "EGL_CONTEXT_PRIORITY_HIGH_IMG",		# 0x3101
    "EGL_CONTEXT_PRIORITY_MEDIUM_IMG",		# 0x3102
    "EGL_CONTEXT_PRIORITY_LOW_IMG",		# 0x3103
    "EGL_BITMAP_PIXEL_SIZE_KHR",		# 0x3110
    "EGL_COVERAGE_SAMPLE_RESOLVE_NV",		# 0x3131
    "EGL_COVERAGE_SAMPLE_RESOLVE_DEFAULT_NV",		# 0x3132
    "EGL_COVERAGE_SAMPLE_RESOLVE_NONE_NV",		# 0x3133
    "EGL_MULTIVIEW_VIEW_COUNT_EXT",		# 0x3134
    "EGL_AUTO_STEREO_NV",		# 0x3136
    "EGL_CONTEXT_OPENGL_RESET_NOTIFICATION_STRATEGY_EXT",		# 0x3138
    "EGL_BUFFER_AGE_KHR",		# 0x313D
    "EGL_PLATFORM_DEVICE_EXT",		# 0x313F
    "EGL_NATIVE_BUFFER_ANDROID",		# 0x3140
    "EGL_PLATFORM_ANDROID_KHR",		# 0x3141
    "EGL_RECORDABLE_ANDROID",		# 0x3142
    "EGL_SYNC_NATIVE_FENCE_ANDROID",		# 0x3144
    "EGL_SYNC_NATIVE_FENCE_FD_ANDROID",		# 0x3145
    "EGL_SYNC_NATIVE_FENCE_SIGNALED_ANDROID",		# 0x3146
    "EGL_FRAMEBUFFER_TARGET_ANDROID",		# 0x3147
    "EGL_CONTEXT_OPENGL_DEBUG",		# 0x31B0
    "EGL_CONTEXT_OPENGL_FORWARD_COMPATIBLE",		# 0x31B1
    "EGL_CONTEXT_OPENGL_ROBUST_ACCESS",		# 0x31B2
    "EGL_CONTEXT_OPENGL_NO_ERROR_KHR",		# 0x31B3
    "EGL_CONTEXT_OPENGL_RESET_NOTIFICATION_STRATEGY_KHR",		# 0x31BD
    "EGL_NO_RESET_NOTIFICATION",		# 0x31BE
    "EGL_LOSE_CONTEXT_ON_RESET",		# 0x31BF
    "EGL_DRM_BUFFER_FORMAT_MESA",		# 0x31D0
    "EGL_DRM_BUFFER_USE_MESA",		# 0x31D1
    "EGL_DRM_BUFFER_FORMAT_ARGB32_MESA",		# 0x31D2
    "EGL_DRM_BUFFER_MESA",		# 0x31D3
    "EGL_DRM_BUFFER_STRIDE_MESA",		# 0x31D4
    "EGL_PLATFORM_X11_KHR",		# 0x31D5
    "EGL_WAYLAND_BUFFER_WL",		# 0x31D5
    "EGL_PLATFORM_X11_SCREEN_KHR",		# 0x31D6
    "EGL_WAYLAND_PLANE_WL",		# 0x31D6
    "EGL_PLATFORM_GBM_KHR",		# 0x31D7
    "EGL_TEXTURE_Y_U_V_WL",		# 0x31D7
    "EGL_PLATFORM_WAYLAND_KHR",		# 0x31D8
    "EGL_TEXTURE_Y_UV_WL",		# 0x31D8
    "EGL_TEXTURE_Y_XUXV_WL",		# 0x31D9
    "EGL_TEXTURE_EXTERNAL_WL",		# 0x31DA
    "EGL_WAYLAND_Y_INVERTED_WL",		# 0x31DB
    "EGL_STREAM_FIFO_LENGTH_KHR",		# 0x31FC
    "EGL_STREAM_TIME_NOW_KHR",		# 0x31FD
    "EGL_STREAM_TIME_CONSUMER_KHR",		# 0x31FE
    "EGL_STREAM_TIME_PRODUCER_KHR",		# 0x31FF
    "EGL_D3D_TEXTURE_2D_SHARE_HANDLE_ANGLE",		# 0x3200
    "EGL_FIXED_SIZE_ANGLE",		# 0x3201
    "EGL_CONSUMER_LATENCY_USEC_KHR",		# 0x3210
    "EGL_PRODUCER_FRAME_KHR",		# 0x3212
    "EGL_CONSUMER_FRAME_KHR",		# 0x3213
    "EGL_STREAM_STATE_KHR",		# 0x3214
    "EGL_STREAM_STATE_CREATED_KHR",		# 0x3215
    "EGL_STREAM_STATE_CONNECTING_KHR",		# 0x3216
    "EGL_STREAM_STATE_EMPTY_KHR",		# 0x3217
    "EGL_STREAM_STATE_NEW_FRAME_AVAILABLE_KHR",		# 0x3218
    "EGL_STREAM_STATE_OLD_FRAME_AVAILABLE_KHR",		# 0x3219
    "EGL_STREAM_STATE_DISCONNECTED_KHR",		# 0x321A
    "EGL_BAD_STREAM_KHR",		# 0x321B
    "EGL_BAD_STATE_KHR",		# 0x321C
    #"EGL_BUFFER_COUNT_NV",		# 0x321D
    "EGL_CONSUMER_ACQUIRE_TIMEOUT_USEC_KHR",		# 0x321E
    "EGL_SYNC_NEW_FRAME_NV",		# 0x321F
    "EGL_BAD_DEVICE_EXT",		# 0x322B
    "EGL_DEVICE_EXT",		# 0x322C
    "EGL_BAD_OUTPUT_LAYER_EXT",		# 0x322D
    "EGL_BAD_OUTPUT_PORT_EXT",		# 0x322E
    "EGL_SWAP_INTERVAL_EXT",		# 0x322F
    "EGL_DRM_DEVICE_FILE_EXT",		# 0x3233
    "EGL_DRM_CRTC_EXT",		# 0x3234
    "EGL_DRM_PLANE_EXT",		# 0x3235
    "EGL_DRM_CONNECTOR_EXT",		# 0x3236
    "EGL_OPENWF_DEVICE_ID_EXT",		# 0x3237
    "EGL_OPENWF_PIPELINE_ID_EXT",		# 0x3238
    "EGL_OPENWF_PORT_ID_EXT",		# 0x3239
    "EGL_LINUX_DMA_BUF_EXT",		# 0x3270
    "EGL_LINUX_DRM_FOURCC_EXT",		# 0x3271
    "EGL_DMA_BUF_PLANE0_FD_EXT",		# 0x3272
    "EGL_DMA_BUF_PLANE0_OFFSET_EXT",		# 0x3273
    "EGL_DMA_BUF_PLANE0_PITCH_EXT",		# 0x3274
    "EGL_DMA_BUF_PLANE1_FD_EXT",		# 0x3275
    "EGL_DMA_BUF_PLANE1_OFFSET_EXT",		# 0x3276
    "EGL_DMA_BUF_PLANE1_PITCH_EXT",		# 0x3277
    "EGL_DMA_BUF_PLANE2_FD_EXT",		# 0x3278
    "EGL_DMA_BUF_PLANE2_OFFSET_EXT",		# 0x3279
    "EGL_DMA_BUF_PLANE2_PITCH_EXT",		# 0x327A
    "EGL_YUV_COLOR_SPACE_HINT_EXT",		# 0x327B
    "EGL_SAMPLE_RANGE_HINT_EXT",		# 0x327C
    "EGL_YUV_CHROMA_HORIZONTAL_SITING_HINT_EXT",		# 0x327D
    "EGL_YUV_CHROMA_VERTICAL_SITING_HINT_EXT",		# 0x327E
    "EGL_ITU_REC601_EXT",		# 0x327F
    "EGL_ITU_REC709_EXT",		# 0x3280
    "EGL_ITU_REC2020_EXT",		# 0x3281
    "EGL_YUV_FULL_RANGE_EXT",		# 0x3282
    "EGL_YUV_NARROW_RANGE_EXT",		# 0x3283
    "EGL_YUV_CHROMA_SITING_0_EXT",		# 0x3284
    "EGL_YUV_CHROMA_SITING_0_5_EXT",		# 0x3285
    "EGL_DISCARD_SAMPLES_ARM",		# 0x3286
    "EGL_PROTECTED_CONTENT_EXT",		# 0x32C0
    "EGL_YUV_BUFFER_EXT",		# 0x3300
    "EGL_YUV_ORDER_EXT",		# 0x3301
    "EGL_YUV_ORDER_YUV_EXT",		# 0x3302
    "EGL_YUV_ORDER_YVU_EXT",		# 0x3303
    "EGL_YUV_ORDER_YUYV_EXT",		# 0x3304
    "EGL_YUV_ORDER_UYVY_EXT",		# 0x3305
    "EGL_YUV_ORDER_YVYU_EXT",		# 0x3306
    "EGL_YUV_ORDER_VYUY_EXT",		# 0x3307
    "EGL_YUV_ORDER_AYUV_EXT",		# 0x3308
    "EGL_YUV_CSC_STANDARD_EXT",		# 0x330A
    "EGL_YUV_CSC_STANDARD_601_EXT",		# 0x330B
    "EGL_YUV_CSC_STANDARD_709_EXT",		# 0x330C
    "EGL_YUV_CSC_STANDARD_2020_EXT",		# 0x330D
    "EGL_YUV_NUMBER_OF_PLANES_EXT",		# 0x3311
    "EGL_YUV_SUBSAMPLE_EXT",		# 0x3312
    "EGL_YUV_SUBSAMPLE_4_2_0_EXT",		# 0x3313
    "EGL_YUV_SUBSAMPLE_4_2_2_EXT",		# 0x3314
    "EGL_YUV_SUBSAMPLE_4_4_4_EXT",		# 0x3315
    "EGL_YUV_DEPTH_RANGE_EXT",		# 0x3317
    "EGL_YUV_DEPTH_RANGE_LIMITED_EXT",		# 0x3318
    "EGL_YUV_DEPTH_RANGE_FULL_EXT",		# 0x3319
    "EGL_YUV_PLANE_BPP_EXT",		# 0x331A
    "EGL_YUV_PLANE_BPP_0_EXT",		# 0x331B
    "EGL_YUV_PLANE_BPP_8_EXT",		# 0x331C
    "EGL_YUV_PLANE_BPP_10_EXT",		# 0x331D
    "EGL_OBJECT_THREAD_KHR",		# 0x33B0
    "EGL_OBJECT_DISPLAY_KHR",		# 0x33B1
    "EGL_OBJECT_CONTEXT_KHR",		# 0x33B2
    "EGL_OBJECT_SURFACE_KHR",		# 0x33B3
    "EGL_OBJECT_IMAGE_KHR",		# 0x33B4
    "EGL_OBJECT_SYNC_KHR",		# 0x33B5
    "EGL_OBJECT_STREAM_KHR",		# 0x33B6
    "EGL_DEBUG_CALLBACK_KHR",		# 0x33B8
    "EGL_DEBUG_MSG_CRITICAL_KHR",		# 0x33B9
    "EGL_DEBUG_MSG_ERROR_KHR",		# 0x33BA
    "EGL_DEBUG_MSG_WARN_KHR",		# 0x33BB
    "EGL_DEBUG_MSG_INFO_KHR",		# 0x33BC
    "EGL_DMA_BUF_PLANE3_FD_EXT",		# 0x3440
    "EGL_DMA_BUF_PLANE3_OFFSET_EXT",		# 0x3441
    "EGL_DMA_BUF_PLANE3_PITCH_EXT",		# 0x3442
    "EGL_DMA_BUF_PLANE0_MODIFIER_LO_EXT",	# 0x3443
    "EGL_DMA_BUF_PLANE0_MODIFIER_HI_EXT",	# 0x3444
    "EGL_DMA_BUF_PLANE1_MODIFIER_LO_EXT",	# 0x3445
    "EGL_DMA_BUF_PLANE1_MODIFIER_HI_EXT",	# 0x3446
    "EGL_DMA_BUF_PLANE2_MODIFIER_LO_EXT",	# 0x3447
    "EGL_DMA_BUF_PLANE2_MODIFIER_HI_EXT",	# 0x3448
    "EGL_DMA_BUF_PLANE3_MODIFIER_LO_EXT",	# 0x3449
    "EGL_DMA_BUF_PLANE3_MODIFIER_HI_EXT",	# 0x344A
    "EGL_COLOR_FORMAT_HI",		# 0x8F70
    "EGL_COLOR_RGB_HI",		# 0x8F71
    "EGL_COLOR_RGBA_HI",		# 0x8F72
    "EGL_COLOR_ARGB_HI",		# 0x8F73
    "EGL_CLIENT_PIXMAP_POINTER_HI",		# 0x8F74
    #"EGL_FOREVER",		# 0xFFFFFFFFFFFFFFFF
])
